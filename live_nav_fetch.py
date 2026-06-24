import requests
import pandas as pd

funds = {

    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841

}

for name, code in funds.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    print("Fetching:", name)

    print("Scheme Name:", data["meta"]["scheme_name"])

    nav_data = data["data"]

    df = pd.DataFrame(nav_data)

    filename = f"data/raw/{name}.csv"

    df.to_csv(filename, index=False)

    print("Saved\n")