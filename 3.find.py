import pymongo

if __name__ == "__main__":
    print("Welcome to pymongo")
    client =pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client["rohit"]
    collection = db["samplecollection"]

    #find one
    one = collection.find_one({"Name":"Rohan"})
    print(one)

    #find all

    allDocs = collection.find({"Name":"Ankit"})   #allDocs = collection.find({"Name":"Ankit"},{"Name":1, "_id": 0})  hyani fkt name distl
    for i in allDocs:
        print(i)