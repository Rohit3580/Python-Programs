import pymongo

if __name__ == "__main__":
    print("Welcome to pymongo")
    client =pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client["rohit"]
    collection = db["samplecollection"]

    #Insertion One
    dictionary = {"name":"Rohit", "marks": 50}
    collection.insert_one(dictionary)

    #insert many
    List1 = [
             {"_id":1,"Name": "Rohan", "City": "Pune", "Marks": 55},
             {"_id":2,"Name": "Akash", "City": "Mumbai", "Marks": 25},
             {"_id":3,"Name": "Navin", "City": "Chennai", "Marks": 35},
             {"_id":4,"Name": "Suraj", "City": "Kolkatta", "Marks": 65},
             {"_id":5,"Name": "Ankit", "City": "Hydrabad", "Marks": 40}
             ]
    collection.insert_many(List1)