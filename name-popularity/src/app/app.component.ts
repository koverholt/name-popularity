import { Component } from '@angular/core';
declare let Plotly: any;

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'name-popularity';
  input_name: any;
  formatted_name_sum: any;
  top_year: any;

  constructor() {
    // URL parameters

    // var param = new Vue({
    //   created() {
    //     let uri = window.location.search.substring(1);
    //     let params = new URLSearchParams(uri);
    //     window.value = params.get("name");
    //   },
    // });

    // Query

    // var input_name = window.value || "Kristopher"
    // var input = { "name": input_name };
    var input = { "name": "Kristopher" };

    var xhr = new XMLHttpRequest();
    var self = this;
    xhr.open("POST", "https://us-central1-koverholt-apps-304316.cloudfunctions.net/name-popularity");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(input));

    xhr.onload = function () {
      var obj = JSON.parse(this.response);
      self.input_name = obj["input_name"];
      self.formatted_name_sum = obj["formatted_name_sum"];
      self.top_year = obj["top_year"];
      var female_count = obj["female_count"];
      var female_year = obj["female_year"];
      var male_count = obj["male_count"];
      var male_year = obj["male_year"];

      var trace1 = {
        x: male_year,
        y: male_count,
        name: "Male",
        type: "bar"
      };

      var trace2 = {
        x: female_year,
        y: female_count,
        name: "Female",
        type: "bar"
      };

      var data = [trace1, trace2];

      var layout = {
        barmode: "stack",
        plot_bgcolor: "rgba(0,0,0,0)",
        paper_bgcolor: "rgba(51,51,51,0)",
        font: {
          color: "white",
        }
      };

      var config = {
        'displayModeBar': false
      };

      Plotly.newPlot("chart", data, layout, config);

    };

  }
}
