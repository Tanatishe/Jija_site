from fastapi import FastAPI

from src.routing.router import router

app=FastAPI()

app.include_router(router,prefix='')