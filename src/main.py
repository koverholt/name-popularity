import os
import zipfile
import pandas as pd

df = pd.read_csv("")

def get_name_info(input_name):
    name_match = df[df["name"] == input_name]
    name_sum = int(name_match["birthcount"].sum())
    formatted_name_sum = '{:,}'.format(name_sum)
    top_year = int(name_match[name_match["birthcount"] == name_match["birthcount"].max()]["year"])

    male_year = name_match[name_match["gender"] == "M"]["year"].tolist()
    male_count = name_match[name_match["gender"] == "M"]["birthcount"].tolist()
    female_year = name_match[name_match["gender"] == "F"]["year"].tolist()
    female_count = name_match[name_match["gender"] == "F"]["birthcount"].tolist()

    result = {
        "input_name": input_name,
        "name_sum": name_sum,
        "formatted_name_sum": formatted_name_sum,
        "top_year": top_year,
        "male_year": male_year,
        "male_count": male_count,
        "female_year": female_year,
        "female_count": female_count,
    }

    return result

def apply(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST',
        'Access-Control-Allow-Headers': 'Content-Type'
    }

    request_json = request.get_json(silent=True)
    input_name = request_json.get("name", "Kristopher")
    input_name = input_name.title()
    result = get_name_info(input_name)
    return (result, 200, headers)
