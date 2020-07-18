# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 10:23:49 2020

@author: VB
"""

import pymongo

client = pymongo.MongoClient()

# Insert to collection

db = client.test
db.sites.insert({"url":"http://www.raydelto.org","name":"Raydelto's Homepage"})

# Read data from mongo

site = db.sites.find_one()

site["name"]

print("I like the %s and the url is %s" %(site['name'],site['url']))

sites = db.sites.find()

for s in sites:
    print(s["name"])
