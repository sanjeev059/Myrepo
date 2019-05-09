

from pymongo import MongoClient
import json
from datetime import timedelta, datetime
import requests

mongo_host = 'dev-turvo-sandbox-20190430.turvo.net:27017'
client = MongoClient(mongo_host)
print client
       #mongo_username = root
       #mongo_password =

Hi need ETA for below tickets
 SUP-5751 --> EDI pranab.d fixed                EDI
 SUP-5744  --> fixed by hitesh                  CORE
 QE-5434,--> @pranab.d                          EDI
 QE-5433,5432,5431,5430 --> @som                V2 Services 
