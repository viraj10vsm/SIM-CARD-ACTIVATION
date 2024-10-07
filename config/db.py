from pymongo import MongoClient
from pymongo.server_api import ServerApi
db_password = "oRFJJy3la3ocx1EU"
uri = f'mongodb+srv://mahaleviraj1018:{db_password}@simact.5hd2h.mongodb.net/?retryWrites=true&w=majority&appName=SIMACT'
conn = MongoClient(uri, server_api=ServerApi('1'))
