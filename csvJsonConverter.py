import json
import csv

with open('source.csv', 'r') as inputFile:
    with open('source.json', 'w') as jsonFile:
        reader = csv.DictReader(inputFile)
        rows = [row for row in reader]
        data = json.dump(rows, jsonFile)
