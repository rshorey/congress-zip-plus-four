import csv
import json
from collections import OrderedDict


changed_members = {}
with open("/home/rachel/work/contact-congress/support/update-to-114th/election_results_2014.csv","r") as results:
    reader = csv.DictReader(results)
    for line in reader:
        if line["member_id"] != line["new_id"]:
            changed_members[line["member_id"]] = {"new_id":line["new_id"], "name":line["new_member"]}

new_json = {}

with open("legislators.json","r") as leg:
    members = json.load(leg)
    for bioguide_id, info in members.items():
        if bioguide_id in changed_members:
            new_id = changed_members[bioguide_id]["new_id"]
            info["name"] = changed_members[bioguide_id]["name"]
            new_json[new_id] = info
        else:
            new_json[bioguide_id] = info

sorted_json = OrderedDict(sorted(new_json.items(), key=lambda t:t[0]))

with open("114th_legislators.json","w") as new_leg:
    new_leg.write(json.dumps(sorted_json, indent=4))