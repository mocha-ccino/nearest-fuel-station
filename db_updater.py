from dotenv import load_dotenv
from fuel_price_getter import download_fuel_data
import pymongo
import os
import json
import logging

load_dotenv()

conn_str = os.environ.get("MONGO_CONNSTR")
client = pymongo.MongoClient(conn_str)

db_log_file = "logs/db_refresh.log"
logging.basicConfig(filename=db_log_file, filemode="a", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

fuel_db = client["fuel_db"]
fuel_col = fuel_db["fuel_col"]

download_fuel_data()
json_dir = os.path.join("fuel-jsons")
fuel_files = os.listdir(json_dir)

# looping through all downloaded files and uploading their station info to the mongo DB

all_stations = []

for file in fuel_files:
    with open(os.path.join(json_dir, file), 'r') as cur_file:
        cur_file = json.load(cur_file)
        cur_stations = cur_file['stations']
        for station in cur_stations:
            all_stations.append(station)

fuel_db.drop_collection("fuel_col")
update = fuel_col.insert_many(all_stations)