from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://nadimwani2:nadim214@cluster0.nycar.mongodb.net/?retryWrites=true&w=majority"

#create a new client and connect to server
client=MongoClient(uri)

#create database name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"

df=pd.read_csv("D:\pw\data science with ml\PROJECT\sensorproject\notebooks\wafer_23012020_041211.csv")

df.drop("Unnamed: 0",axis=1,inplace=True)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

