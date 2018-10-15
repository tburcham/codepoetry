import requests

r = requests.get(url)

data = r.json()

data["results"]["total_num_results"]
