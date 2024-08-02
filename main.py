import os
from dotenv import load_dotenv

from fastapi import FastAPI
from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator

load_dotenv()

app = FastAPI()


def get_cluster():
    return Cluster("couchbase://localhost",
                  authenticator=PasswordAuthenticator(os.environ.get("USERNAME"), os.environ.get("PASSWORD")))


def get_inventory_collection():
    collection = get_cluster().bucket("personalized-blogs").scope("inventory")
    return collection


@app.get("/")
async def root():
    return {'message': 'Hello world'}