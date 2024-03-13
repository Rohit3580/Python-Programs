import pymongo

if __name__ == "__main__":
    print("Welcome to pymongo")
    client =pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    
    a = client.list_database_names()
    print(a)

    