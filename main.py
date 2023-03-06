#pip install fastapi uvicorn
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
  dummy_data = {"word": "Hello world"}
  return dummy_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)