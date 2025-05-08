from fastapi import FastAPI
from routers import trademark_router

app = FastAPI(title="Trademark Search API")

app.include_router(trademark_router.router)