import json
import sys

args = sys.argv

with open(args[1]) as data_file:
    data = json.load(data_file)

# find listid of 'DONE:Today'
for l in data['lists']:
    if l['title'] == 'DONE:Today':
        doneListId = l['_id']

# print out card contents of list 'DONE:Today'
for c in data['cards']:
    if c['listId'] == doneListId:
        print(c['title'])
