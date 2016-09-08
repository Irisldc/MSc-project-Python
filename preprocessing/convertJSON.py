import json
from pprint import pprint

with open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviews_Movies_and_TV_5.json') as json_data:
    data=json.load(json_data)

pprint(data)