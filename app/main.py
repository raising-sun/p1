import fastapi
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange


app = FastAPI()

my_posts = [{"title": "t1", "content": "1st post", "id": 1},
            {"title": "t2", "content": "2st post", "id": 2} ]

class Post(BaseModel):
    title: str
    content: str
    id: int | None = None

def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p

def find_index(id: int):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def main():
    print("Hello from p1!")
    return {"mess": "hell"}

@app.get("/posts")
def posts():
    print("Hello from p1!")
    return {"pots": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(data: Post):
    data1 = data.model_dump()
    data1['id'] = randrange(0, 10000)
    #print(data.title)
    #print(data)
    my_posts.append(data1)
    return {"newPost": data1}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    # print(type(id))
    # id = int(id)
    # print(type(id))
    p = find_post(id)
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": "id not found"}
    return {"message":"retreived", "post":p}

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id does not exist")
    else:
        my_posts.pop(index)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id does not exist")
    else:
        data = post.model_dump()
        data["id"] = id
        my_posts[index] = data
        return {"updataed post": data}

    
#print(fastapi.__version__)


#if __name__ == "__main__":
#    main()
