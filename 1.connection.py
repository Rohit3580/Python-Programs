import pymongo

if __name__ == "__main__":
    print("Welcome to pymongo")
    client =pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client["rohit"]
    collection = db["samplecollection"]

    