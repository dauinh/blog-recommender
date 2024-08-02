import os
from dotenv import load_dotenv
from datetime import datetime

from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator

load_dotenv()

cluster = Cluster("couchbase://localhost",
                  authenticator=PasswordAuthenticator(os.environ.get("USERNAME"), os.environ.get("PASSWORD")))
bucket = cluster.bucket("travel-sample")
hotel_collection = bucket.scope("inventory").collection("hotel")


def insert():
    print("[kv-insert]")
    # tag::kv-insert[]
    # Create a document object.
    document = {
        "id": 123,
        "name": "Medway Youth Hostel",
        "address": "Capstone Road, ME7 3JE",
        "url": "http://www.yha.org.uk",
        "geo": {
            "lat": 51.35785,
            "lon": 0.55818,
            "accuracy": "RANGE_INTERPOLATED",
        },
        "country": "United Kingdom",
        "city": "Medway",
        "state": None,
        "reviews": [
            {
                "content": "This was our 2nd trip here and we enjoyed it more than last year.",
                "author": "Ozella Sipes",
                "date": datetime.now().isoformat(),
            },
        ],
        "vacancy": True,
        "description": "40 bed summer hostel about 3 miles from Gillingham.",
    }

    # Insert the document in the hotel collection.
    insert_result = hotel_collection.insert("hotel-123", document)

    # Print the result's CAS metadata to the console.
    print("CAS:", insert_result.cas)