from fastapi import Depends, FastAPI
from models.Token import Token
from models.User import User
from models.Story import Story
from services.Stories import create_stories, delete_story, get_stories, update_story
from services.User import create_user, get_users, update_user, delete_user, authenticate_user
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn

from dotenv import load_dotenv
import os

load_dotenv()

db_password = os.getenv("DB_PASSWORD")


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/create-user")
def create_new_user(user : User):
    return create_user(user)

@app.get("/get-users")
def get_all_users():
    return get_users()

@app.put("/update-user/{id}")
def update_user_by_id(id: int, user : User):
    return update_user(id, user)

@app.delete("/delete-user/{id}")
def delete_user_by_id(id: int):
    return delete_user(id)

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return authenticate_user(form_data.username, form_data.password)

@app.post("/create-story")
def create_new_story(story : Story, token: str = Depends(oauth2_scheme)):
    return create_stories(story)

@app.get("/get-stories")
def get_all_stories():
    return get_stories()

@app.put("/update-story/{id}")
def update_story_by_id(id: int, story : Story):
    return update_story(id, story)

@app.delete("/delete-story/{id}")
def delete_story_by_id(id: int):
    return delete_story(id)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


