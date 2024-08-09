import os
import logging
from datetime import timedelta
from dotenv import load_dotenv

from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator
from couchbase.options import QueryOptions, ClusterOptions

load_dotenv()
logger = logging.getLogger()
username = "admin"
password = "B8r~*f7RV5)$UFj"
endpoint = "couchbase://localhost"
bucket_name = "blog-recommender"

auth = ClusterOptions(PasswordAuthenticator(username, password))
cluster = Cluster(endpoint, auth)

# Wait until the cluster is ready for use.
cluster.wait_until_ready(timedelta(seconds=3))

logger.info("Cluster ready.")

inventory = cluster.bucket(bucket_name).scope("inventory")


def get_all(collection: str = "user" or "blog"):
    result = cluster.query(
        f"SELECT * FROM `blog-recommender`.`inventory`.`{collection}`"
    )
    try:
        return list(result)
    except Exception:
        print("No rows found")


def get_user_by_id(user_id):
    result = cluster.query(
        f"""SELECT * FROM `blog-recommender`.`inventory`.`user` WHERE id = {user_id}"""
    )
    try:
        return list(result)[0]
    except IndexError:
        print("User not found")


def get_user_history(user_id):
    result = cluster.query(
        f"""SELECT blog
            FROM `blog-recommender`.`inventory`.`blog` blog, `blog-recommender`.`inventory`.`user` u
            WHERE blog.id IN u.history AND u.id == {user_id}"""
    )
    try:
        return list(result)
    except IndexError:
        print("User not found")


def get_recommendations(user_id):
    user_profile = get_user_by_id(user_id)["user"]
    result = cluster.query(
        """SELECT * FROM `blog-recommender`.`inventory`.`blog`
            WHERE category IN $preferences AND id NOT IN $history""",
        QueryOptions(
            named_parameters={
                "preferences": user_profile["preferences"],
                "history": user_profile["history"],
            }
        ),
    )
    try:
        return list(result)
    except Exception:
        print("No rows found")


def update_preference(user_id, input):
    result = cluster.query(
        f"""UPDATE `blog-recommender`.`inventory`.`user` u
            SET u.preferences = ARRAY_APPEND(u.preferences, "{input}")
            WHERE u.id = {user_id}
            RETURNING u.preferences;"""
    )
    try:
        return result
    except Exception:
        print("Preference cannot be updated")


def seeding():
    users = {
        "user1": {
            "id": 1,
            "name": "human",
            "preferences": ["technology", "cooking"],
            "history": [1],
        },
        "user2": {
            "id": 2,
            "name": "alien",
            "preferences": ["technology", "earth"],
            "history": [3],
        },
    }
    blogs = {
        "blog1": {
            "id": 1,
            "title": "Latest Tech Trends",
            "category": "technology",
            "tags": ["AI", "ML", "innovation"],
        },
        "blog2": {
            "id": 2,
            "title": "How to create your own pasta recipes",
            "category": "cooking",
            "tags": ["pasta", "sauces"],
        },
        "blog3": {
            "id": 3,
            "title": "Future of Earth",
            "category": "earth",
            "tags": ["global warming", "space exploration"],
        },
        "blog4": {
            "id": 4,
            "title": "Understanding Arts",
            "category": "arts",
            "tags": ["visual arts", "perfomance arts"],
        },
        "blog5": {
            "id": 5,
            "title": "Programming 101",
            "category": "technology",
            "tags": ["Python"],
        },
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
