import json

for a in open('item.txt', 'r', encoding='utf-8'):
    b = a.split('}{')
b[0] = b[0] + '}'
b[-1] = '{' + b[-1]
for i in range(1, len(b) - 1):
    b[i] = '{' + b[i] + '}'
b = [eval(x) for x in b]
for x in b:
    print(x)

import pymongo
database_name = 'Tiki_2'
client = pymongo.MongoClient('localhost', 27017)
database = client[database_name]
collection = database['Item']
collection.insert_many(b)