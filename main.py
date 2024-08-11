from fastapi import FastAPI

from db import get_all, get_user_by_id, get_user_history, get_recommendations, update_preference

app = FastAPI()


@app.get("/users")
def all_users():
    users = get_all("user")
    if not users:
        return {"message": "No user found"}
    return users


@app.get("/users/{user_id}")
def user_by_id(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return {"message": f"User with id {user_id} not found"}
    return user


@app.get("/users/{user_id}/history")
def blog_history(user_id):
    history = get_user_history(user_id)
    if not history:
        return {"message": f"User with id {user_id} has no history"}
    return history


@app.get("/users/{user_id}/recommendations")
def recommendations(user_id):
    return get_recommendations(user_id)


@app.put("/users/{user_id}/")
def preference(user_id, preference):
    print(preference)
    return update_preference(user_id, preference)


@app.get("/blogs")
def all_blogs():
    blogs = get_all("blog")
    if not blogs:
        return {"message": "No blog found"}
    return blogs