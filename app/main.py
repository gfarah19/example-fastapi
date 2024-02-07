from fastapi import FastAPI
from app.models import Base
from .database import engine
from .routers import post, user, auth
from . import models
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


print(settings.database_password)

#models.Base.metadata.create_all(bind=engine) <- this is if you're not using alembic for models migration

app = FastAPI()

#this is your white list
origins=["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#this is just defining our data schema        

     

#posts = db.query(models.Post).all(), db is the postgres db, query is to search, models.Post is directing to the table, and all is for all the rows


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


#@app.get("/")
#def test():
#    post = "it worked!"
#    return{"post_details": post}
