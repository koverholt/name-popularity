import Algorithmia
import os
import requests
import zipfile
import pandas as pd

os.mkdir("data")
os.mkdir("download")

download_file = "download/names.zip"
data_path = "data/"

if not os.path.isfile(download_file):
    r = requests.get("https://www.ssa.gov/oact/babynames/names.zip", stream=True)
    with open(download_file, "wb") as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

with zipfile.ZipFile(download_file, "r") as zip_ref:
    zip_ref.extractall(data_path)

file_list = [int(f[3:7]) for f in os.listdir(data_path) if f.endswith(".txt")]
min_year = min(file_list)
max_year = max(file_list)

columns = ["name", "gender", "birthcount"]
df = pd.DataFrame(columns=columns)

for year in range(min_year, max_year+1):
    path = data_path + "yob{}.txt".format(year)
    df_new = pd.read_csv(path, names=columns)
    df_new["year"] = year
    df_new["year"] = df_new["year"].astype(str)
    df = df.append(df_new, ignore_index=True)

df.to_csv("data.csv", index=False)
