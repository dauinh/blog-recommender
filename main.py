from fastapi import FastAPI

from db import get_all

app = FastAPI()


@app.get("/users")
def get_all_users():
    users = get_all("user")
    if not users:
        return {'message': 'No user found'}
    return list(users)


@app.get("/blogs")
def get_all_blogs():
    blogs = get_all("blog")
    if not blogs:
        return {'message': 'No blog found'}
    return list(blogs)