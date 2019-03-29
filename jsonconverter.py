import csv
import json

# Read csv via dictionary
data = {}
with open("details.csv") as csvfile:
	csvreader = csv.DictReader(csvfile)
	for csvrow in csvreader:
		csvid = csvrow["iD"]
		data[csvid] = csvrow

# Write to json
with open("jsondata.json", "w") as jsonfile:
	jsonfile.write(json.dumps(data, indent = 4))