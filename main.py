import os
from dotenv import load_dotenv

from fastapi import FastAPI
from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator
from couchbase.options import ClusterOptions, QueryOptions

load_dotenv()

app = FastAPI()


def get_cluster():
    return Cluster("couchbase://localhost",
                  authenticator=PasswordAuthenticator(os.environ.get("USERNAME"), os.environ.get("PASSWORD")))


def get_inventory():
    return get_cluster().bucket("personalized-blogs").scope("inventory")


def get_all():
    result = get_cluster().query(
        "SELECT * FROM `personalized-blogs`.`inventory`.`user` LIMIT 10", QueryOptions(metrics=True))

    if result.rows():
        for row in result.rows():
            print(f"Found row: {row}")
    else:
        print('No row found')

    print(f"Report execution time: {result.metadata().metrics().execution_time()}")


def seeding():
    document = {
        "id": 1,
        "name": "human",
        "preferences": ["technology", "cooking"],
        "history": ["article1", "article2"]
    }
    user_collection = get_inventory().collection("user")
    result = user_collection.insert("user1", document)
    print("CAS:", result.cas)


@app.get("/")
async def root():
    get_all()
    return {'message': 'Hello world'}