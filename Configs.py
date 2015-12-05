import json


for key, val in json.load(open('configs.json')).iteritems():
    globals()[key] = val