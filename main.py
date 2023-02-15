import csv
import json
import requests

url = 'https://api.segment.io/v1/track'
API_KEY = 'Basic Q3hNWVVReVlCQXYzdUZJeUN1enMxeWN0WDJKSkhGZEY6'

headers = {
    'Content-Type': 'application/json',
    'Authorization': API_KEY
}

with open('batch_test_15.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if len(row) == 0:
            continue
        temp = row[0].split(",")
        if temp[0] == "userId":
            continue

        body = json.dumps({"userId": temp[0],
                           "event": "Order Completed",
                           "properties": {
                             "products": temp[1].split("|")
                           },
                           "timestamp": temp[2]
                         })

        response = requests.post(url, data=body, headers=headers)
        print(response.json())