from fastapi import FastAPI
from app.api.establishments import router as establishments_router


app = FastAPI()
app.include_router(establishments_router)


@app.get("/")
def root():
    return {"message": "API is running"}
