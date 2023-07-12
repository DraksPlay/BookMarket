from fastapi import FastAPI
from api.router import router
from config import API_PATH

app = FastAPI(docs_url=f"{API_PATH}/docs")


app.include_router(router, prefix=API_PATH)
