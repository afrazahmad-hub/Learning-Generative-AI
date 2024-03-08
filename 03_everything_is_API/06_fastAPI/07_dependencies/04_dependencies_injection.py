from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated

# https://www.youtube.com/watch?v=0c4NFdpu2vY&t=69s

# data of blogs in dict form
blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

users = {
    "8": "Ahmed",
    "9": "Mohammed"
}

# creating class to call the dependencies
class GetObjOr404:
    def __init__(self, model):
        self.model = model

    def __call__(self, id:str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object id {id} not found")
        else:
            return obj

app: FastAPI = FastAPI()


# # function to get blog name against id
# def get_blog_or_404(id: str):
#     blog = blogs.get(id)
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
#     else:
#         return blog


# instance for blog dependencies
blog_dependencies = GetObjOr404(blogs)

# running the server
@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependencies)]):
    return {"blog_name": blog_name}

# instance for user dependencies
user_dependencies = GetObjOr404(users)

# running the server
@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(user_dependencies)]):
    return {"user_name": user_name}