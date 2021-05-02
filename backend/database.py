from pymongo import MongoClient

DATABASE = MongoClient('localhost', 27017)
db = DATABASE['barber']