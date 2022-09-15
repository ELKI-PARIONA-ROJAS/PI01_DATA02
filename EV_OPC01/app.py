from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="My first API",
    description="This is my first API",
    version="1.0.0",
    openapi_tags=[{
        "name": "users",
        "description": "Operations with users."
    }]
)

app.include_router(user)
