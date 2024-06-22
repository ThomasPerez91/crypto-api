from fastapi import FastAPI  # type: ignore
from routes import router as api_router


app = FastAPI()
app.include_router(api_router)


@app.get('/')
def read_root():
    return {"message": "Hello World"}
