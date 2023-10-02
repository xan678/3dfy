import motor.motor_asyncio

def startMongoClient(uri):
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)

    try:
        client.admin.command('ping')
        print("MongoDB connection succeeded!!!")
    except Exception  as e:
        print(e)