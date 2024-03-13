import pymongo

if __name__ == "__main__":
    print("Welcome to pymongo")
    client =pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client["rohit"]
    collection = db["samplecollection"]

    prev = {"Name": "Rohan"}
    nextt = {"$set":{"City":"Kerala"}}

    #update one record
    collection.update_one(prev,nextt)

    #update many 
    prev = {"Name": "Akash"}
    nextt = {"$set":{"City": "Netharland"}}
    ino = collection.update_many(prev,nextt)
    print("No. of document update:",ino.modified_count)
    

    