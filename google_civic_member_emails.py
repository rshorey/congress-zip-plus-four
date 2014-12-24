import requests
import json
from google_api_key import API_KEY

legislators = "legislators.json"

base_url = "https://www.googleapis.com/civicinfo/v2/representatives?address=1%s&levels=country&key="+API_KEY


emails = {}

with open(legislators, 'r') as leg:
    districts = json.loads(leg.read())
    

    for bioguide, d in districts.items():
        address = "+".join([d["example_address"], d["example_city"], d["example_state"]]).replace(" ","+")

        url = base_url % address
        r = requests.get(url)
        try:
            leg_json = r.json()["officials"]
        except KeyError:
            print address
            print("Legislator %s, %s doesn't seem to be working" % (bioguide,d["name"]))
        else:
            for person in leg_json:
                if "emails" in person:
                    emails[person["name"]] = person["emails"][0]



