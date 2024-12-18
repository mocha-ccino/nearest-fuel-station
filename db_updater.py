from dotenv import load_dotenv
from fuel_price_getter import download_fuel_data
import pymongo
import os
import json
import logging

os.makedirs("logs", exist_ok=True)

# logger configuration
db_log_file = "logs/db_refresh.log"
logger = logging.getLogger("refresh_logger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(db_log_file, mode="a")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def db_refesher(conn_str: str) -> None:
    """
    Downloads all the fuel data once more, and refreshes the Mongo database with it, making sure to convert locations to 2dsphere indexes first.
    """

    client = pymongo.MongoClient(conn_str)
    fuel_db = client["fuel_db"]
    fuel_col = fuel_db["fuel_col"]

    download_fuel_data()
    json_dir = os.path.join("fuel-jsons")
    fuel_files = os.listdir(json_dir)

    # looping through all downloaded files and uploading their station info to the mongo DB

    all_stations = []

    logger.info("Starting processing...")
    for file in fuel_files:
        logger.info(f"Opening file: {file}")
        with open(os.path.join(json_dir, file), "r") as cur_file:
            cur_file = json.load(cur_file)
            cur_stations = cur_file["stations"]
            for station in cur_stations:

                station["location"] = {
                    "type": "Point",
                    "coordinates": [
                        float(station["location"]["longitude"]),
                        float(station["location"]["latitude"]),
                    ],
                }
                all_stations.append(station)
        logger.info("File finished.")

    fuel_col.delete_many({})
    fuel_col.create_index([("location", "2dsphere")])
    update = fuel_col.insert_many(all_stations)
