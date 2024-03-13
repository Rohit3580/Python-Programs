import pymongo

if __name__ == "__main__":
    print("Welcome to pymongo")
    client =pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client["rohit"]
    collection = db["samplecollection"]

    rec = {"name": "Rohit"}
    
    #delete one record
    #collection.delete_one(rec)

    #update many 
    rec = {"name": "Rohit"}
    ino = collection.delete_many(rec)
    print("No. of delete document:",ino.deleted_count)
    

    