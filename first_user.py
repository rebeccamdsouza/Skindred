import pymongo
from pprint import pprint
from datetime import datetime

# collection - username
# document - speaker(bot,user),timestamp,content

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["skindred"]
col = db["rebecca"]

starting_chat = {
    "speaker": "bot",
    "timestamp": datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"),
    "message": "Hello! I am Skindred! Send me your derma doubts!",
}

col.insert_one(starting_chat)

for x in client.skindred['rebecca'].find({}):
    pprint(x)
