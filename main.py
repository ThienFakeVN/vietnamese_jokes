from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from vietnamesejokes.vietnamese_jokes.jokes import JOKES
from random import choice

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def im_ROOTin_for_ya(): return {"API": "gifted power", "root": "pure effort"}

@app.get("/joke")
def all_jokes(): return JOKES

@app.get("/random_joke")
def random_joke():
    thanhbinh = [x for x in range(len(JOKES))]
    return JOKES[choice(thanhbinh)]

@app.get("/joke/:{id}")
def joke_by_id(id: int): return JOKES[id - 1]

@app.get("/joke/{topic}")
def joke_by_topic(topic: str):
    thanhbinh = []
    x = 0
    while x < len(JOKES):
        if JOKES[x]["chủ đề"] == topic: thanhbinh.append(JOKES[x])
        x += 1
    return thanhbinh

@app.get("/random_joke/{topic}")
def random_joke_by_topic(topic: str): return choice(joke_by_topic(topic))

# uvicorn main:app --reload
