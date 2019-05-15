from pymongo import MongoClient
import json
from datetime import timedelta, datetime
import requests
import datetime as DT
today = DT.date.today()
import dateutil.parser
import subprocess


mongo_host = '192.168.1.145:27017'
mongo_username = None
mongo_password = None

client = MongoClient(mongo_host)

db = client.turvo
print db
data = db.list_collection_names()

print data
#connection = pymongo.Connection('192.168.1.145:27017')
#db = connection['localhost']


prv_date = today - DT.timedelta(days=2)
print prv_date
week_ago = today - DT.timedelta(days=1)
print week_ago


'''
try:
    conn=pymongo.MongoClient('192.168.1.145:27017')
    db=conn.mnemosyne
    data_ip=db.userNotifications.remove({'processFinishTime' : {"$lte" : ISODate("prv_dateTOweek_ago")}})
    for f in data_ip:
        print f['_id']

except pymongo.errors.ConnectionFailure, e:
    print "Could not connect to MongoDB: %s" % e


mongo_host = '192.168.1.145:27017'
mongo_username = None
mongo_password = None
client = MongoClient(mongo_host)
print client

prv_date = today - DT.timedelta(days=2)
print prv_date
week_ago = today - DT.timedelta(days=1)
print week_ago
client.userNotifications.remove({'processFinishTime' : {"$lte" : ISODate("prv_dateTOweek_ago")}})
client.activitiesData.remove({'processFinishTime' : {"$lte" : ISODate("prv_dateTOweek_ago")}})
'''
