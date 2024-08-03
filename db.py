import os
from dotenv import load_dotenv

from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator
from couchbase.options import ClusterOptions, QueryOptions

load_dotenv()


cluster = Cluster("couchbase://localhost",
                  authenticator=PasswordAuthenticator(os.environ.get("USERNAME"), os.environ.get("PASSWORD")))
inventory = cluster.bucket("personalized-blogs").scope("inventory")


def get_all(collection: str = "user" or "blog"):
    result = cluster.query(
        f"SELECT * FROM `personalized-blogs`.`inventory`.`{collection}`", QueryOptions(metrics=True))
    try:
        return result
    except Exception:
        print('No rows found')


def seeding():
    users = {
        "user1": {
            "id": 1,
            "name": "human",
            "preferences": ["technology", "cooking"],
            "history": ["article1", "article2"]
        },
        "user2": {
            "id": 2,
            "name": "alien",
            "preferences": ["technology", "earth"],
            "history": ["article1", "article3"]
        }
    }
    blogs = {
        "article1": {
            "id": "1",
            "title": "Latest Tech Trends",
            "category": "technology",
            "tags": ["AI", "ML", "innovation"]
        },
        "article2": {
            "id": "2",
            "title": "How to create your own pasta recipes",
            "category": "cooking",
            "tags": ["pasta", "sauces"]
        },
        "article3": {
            "id": "3",
            "title": "Future of Earth",
            "category": "earth",
            "tags": ["global warming", "space exploration"]
        },
        "article4": {
            "id": "4",
            "title": "Understanding Arts",
            "category": "arts",
            "tags": ["visual arts", "perfomance arts"]
        },
        "article5": {
            "id": "5",
            "title": "Programming 101",
            "category": "technology",
            "tags": ["Python"]
        }
    }
    user_collection = inventory.collection("user")
    user_collection.insert_multi(users)
    for key in users:
        print("Inserted Document:", key)

    blog_collection = inventory.collection("blog")
    blog_collection.insert_multi(blogs)
    for key in blogs:
        print("Inserted Document:", key)


if __name__ == "__main__":
    seeding()