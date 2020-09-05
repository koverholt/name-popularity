import Algorithmia
import os
import zipfile
import pandas as pd

client = Algorithmia.client()
df = pd.read_csv(client.file("data://koverholt/PopularNames/data.csv").getFile())


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


def apply(input):
    input_name = input.get("name", "Kristopher")
    input_name = input_name.title()
    result = get_name_info(input_name)
    return result
