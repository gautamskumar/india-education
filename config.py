import pymongo
from pymongo import MongoClient

# MongoDB Configuration data
def get_db():
    # client = MongoClient('mongodb://ahan:a1b2c3d4@ds041144.mlab.com:41144/heroku_7wgzzg5m')
    # db = client.heroku_7wgzzg5m

    client = MongoClient(
        'mongodb://heroku_cqkwtd96:mbjehhqholuk690nbcsp96tols@ds039115.mlab.com:39115/heroku_cqkwtd96')
    db = client.heroku_cqkwtd96
    return db