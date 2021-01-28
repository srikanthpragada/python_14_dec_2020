import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")

if resp.status_code != 200:
    print("Sorry! Could not get details of countries!")
    exit()

countries = resp.json()  # Convert JSON to Dict
for country in sorted(countries, key=lambda d: d['population'], reverse=True)[:10]:
    print(f"{country['name']:55} {country['capital']:30} {country['population']:10}")
