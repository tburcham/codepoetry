import requests
from pprint import pprint

word = "coffee"
# r = requests.get("http://api.conceptnet.io/c/en/" + word)
r = requests.get("http://api.conceptnet.io/c/en/" + word + "?rel=/r/IsA&limit=1000")
data = r.json()

#print(data)

for edge in data["edges"]:
    if edge["rel"]["label"] == "HasProperty":
        print(edge["end"]["label"])
