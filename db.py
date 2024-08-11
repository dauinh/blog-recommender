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

logger.info('Cluster ready.')

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
        f"""SELECT * FROM `blog-recommender`.`inventory`.`user` WHERE user_id = {user_id}"""
    )
    try:
        return list(result)[0]
    except IndexError:
        print("User not found")


def get_user_history(user_id):
    result = cluster.query(
        f"""SELECT blog
            FROM `blog-recommender`.`inventory`.`blog` blog, `blog-recommender`.`inventory`.`user` u
            WHERE blog.blog_id IN u.history AND u.user_id == {user_id}"""
    )
    try:
        return list(result)
    except IndexError:
        print("User not found")


def get_recommendations(user_id):
    user_profile = get_user_by_id(user_id)["user"]
    result = cluster.query(
        """SELECT * FROM `blog-recommender`.`inventory`.`blog`
            WHERE topic IN $topics AND id NOT IN $history""",
        QueryOptions(
            named_parameters={
                "topics": user_profile["topics"],
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
            SET u.topics = ARRAY_APPEND(u.topics, "{input}")
            WHERE u.user_id = {user_id}
            RETURNING u.topics;"""
    )
    try:
        return result
    except Exception:
        print("Preference cannot be updated")


def seeding():
    users = {
        "user1": {
            "user_id": 1,
            "topics": ["technology", "cooking"],
            "history": [1],
        },
        "user2": {
            "user_id": 2,
            "topics": ["technology", "earth"],
            "history": [3],
        },
    }
    blogs = {
        "blog1": {
            "blog_id": 1,
            "title": "Latest Tech Trends",
            "topic": "technology",
            "tags": ["AI", "ML", "innovation"],
        },
        "blog2": {
            "blog_id": 2,
            "title": "How to create your own pasta recipes",
            "topic": "cooking",
            "tags": ["pasta", "sauces"],
        },
        "blog3": {
            "blog_id": 3,
            "title": "Future of Earth",
            "topic": "earth",
            "tags": ["global warming", "space exploration"],
        },
        "blog4": {
            "blog_id": 4,
            "title": "Understanding Arts",
            "topic": "arts",
            "tags": ["visual arts", "perfomance arts"],
        },
        "blog5": {
            "blog_id": 5,
            "title": "Programming 101",
            "topic": "technology",
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