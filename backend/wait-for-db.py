import time
import pymongo
from pymongo.errors import ConnectionFailure

def wait_for_mongo(host, port):
    client = pymongo.MongoClient(host, port)
    while True:
        try:
            client.admin.command('ismaster')
            print("MongoDB is ready!")
            break
        except ConnectionFailure:
            print("MongoDB not ready yet, retrying...")
            time.sleep(2)

if __name__ == '__main__':
    wait_for_mongo('mongo', 27017)
