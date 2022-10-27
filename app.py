from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status_code": 200,
        "message": "Successfully hit the API",
    }