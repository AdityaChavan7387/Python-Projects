from fastapi import FastAPI

app = FastAPI()

@app.get("/Health")
def root():
    return {"status": "FastAPI is working!"}
