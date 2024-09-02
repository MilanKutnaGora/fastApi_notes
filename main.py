from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import json
import os
import requests

app = FastAPI()

# OAuth2 setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# User data (hardcoded for simplicity)
users_db = {
    "user1": "password1",
    "user2": "password2",
}


# Note model
class Note(BaseModel):
    title: str
    content: str


# In-memory storage for notes
notes_db = {}


# Function to validate spelling using Yandex Speller API
def validate_spelling(text: str) -> bool:
    response = requests.get(f"https://speller.yandex.net/services/spellservice.json/checkText?text={text}")
    return not response.json()


# Dependency to get current user
def get_current_user(token: str = Depends(oauth2_scheme)):
    user = token.split(":")[0]  # Simplified user extraction from token
    if user not in users_db:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return user


@app.post("/notes/")
async def add_note(note: Note, user: str = Depends(get_current_user)):
    if not validate_spelling(note.title) or not validate_spelling(note.content):
        raise HTTPException(status_code=400, detail="Spelling errors detected in note")

    if user not in notes_db:
        notes_db[user] = []

    notes_db[user].append(note.dict())
    save_notes_to_file()
    return {"message": "Note added successfully"}


@app.get("/notes/")
async def get_notes(user: str = Depends(get_current_user)):
    return {"notes": notes_db.get(user, [])}


def save_notes_to_file():
    with open('notes.json', 'w') as f:
        json.dump(notes_db, f)


# Load existing notes from file at startup
if os.path.exists('notes.json'):
    with open('notes.json', 'r') as f:
        notes_db = json.load(f)

# To run the application, use the command: uvicorn main:app --reload
