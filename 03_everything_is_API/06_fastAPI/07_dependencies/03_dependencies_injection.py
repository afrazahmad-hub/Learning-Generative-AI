from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated

# https://www.youtube.com/watch?v=0c4NFdpu2vY&t=69s


# data of blogs in dict form
blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

app: FastAPI = FastAPI()

# function to get blog name against id
def get_blog_or_404(id: str):
    blog = blogs.get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    else:
        return blog

# running the server
@app.get("/blog/{id}")
def get_blog(blog_name: str = Depends(get_blog_or_404)):
    return {"blog_name": blog_name}

# run the following URl
# http://127.0.0.1:8000/blog/1