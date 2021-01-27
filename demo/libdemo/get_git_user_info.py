import requests

user = input("Enter git username :")
resp = requests.get(f"https://api.github.com/users/{user}")

if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

details = resp.json()  # Convert JSON to Dict
for k, v in details.items():
    print(f"{k:20} {v}")
