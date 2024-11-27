import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URI=os.getenv("MONGO_DB_URI")

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from data2conversion.exception.exception import CustomException
from data2conversion.logging.logger import logging

class DataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
        
    def csv_to_json(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URI)
            self.database = self.mongo_client[self.database]
            
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=='__main__':
    FILE_PATH="data/KAG_conversion_data.csv"
    DATABASE="SUSHIL"
    Collection="SalesData"
    dataobj=DataExtract()
    records=dataobj.csv_to_json(file_path=FILE_PATH)
    print("Records got converted to JSON")
    #logging.info("Records got converted to JSON")
    no_of_records=dataobj.insert_data_mongodb(records,DATABASE,Collection)
    print("Data has been succesfully inserted into the MONGODB")    
    #logging.info("Data has been succesfully inserted into the MONGODB")

