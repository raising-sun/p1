import fastapi
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

@app.get("/")
def main():
    print("Hello from p1!")
    return {"mess": "hell"}

@app.get("/posts")
def posts():
    print("Hello from p1!")
    return {"mess": "available posts"}

@app.post("/posts")
def create_posts(data: Post):
    print(data.title)
    return {"newPost": data}

print(fastapi.__version__)


#if __name__ == "__main__":
#    main()
