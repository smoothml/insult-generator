import json

import uvicorn
from fastapi import Depends, FastAPI

from insult_generator.interfaces import InsultDB
from insult_generator.use_cases import insult_anyone, insult_someone

app = FastAPI()


def get_db():
    return InsultDB()


@app.get("/")
async def heartbeat():
    return json.dumps({"message": "I'm alive! Are you ready to be insulted?"})


@app.get("/insult")
async def insult(name: str = None, db: InsultDB = Depends(get_db)):
    if name is not None:
        insult_to_use = insult_someone(db, name)
    else:
        insult_to_use = insult_anyone(db)
    return json.dumps({"message": insult_to_use})


def run():
    uvicorn.run("insult_generator.app:app", host="0.0.0.0", port=8000)
