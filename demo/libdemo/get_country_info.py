import requests


def get_country_by_code(code, countries):
    for c in countries:
        if c['alpha3Code'] == code:
            return c

    return None  # Country code not found


def get_country_name(code, countries):
    for c in countries:
        if c['alpha3Code'] == code:
            return c['name']

    return None  # Country code not found


def get_country_neighbors(country, countries):
    names = []
    for code in country['borders']:
        name = get_country_name(code, countries)
        names.append(name)

    return ",".join(names)


def get_country_currencies(country):
    names = []
    for c in country['currencies']:
        names.append(c['name'])

    return ",".join(names)


resp = requests.get("https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    print("Sorry! Could not get details of countries!")
    exit(1)

countries = resp.json()  # Convert JSON to Dict

code = input("Enter country code :")
country = get_country_by_code(code, countries)
if country is None:
    print("Sorry! Invalid country code!")
    exit(2)

print("Name       : ", country['name'])
print("Capital    : ", country['capital'])
print("Region     : ", country['region'])
print("Neighbors  : ", get_country_neighbors(country, countries))
print("Currencies : ", get_country_currencies(country))
