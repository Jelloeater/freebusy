import logging
import os

import uvicorn

if os.getenv("LOG_LEVEL") is None:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=os.getenv("LOG_LEVEL"))
    print(f'LOG_LEVEL={os.getenv("LOG_LEVEL")}')

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


def start_server():
    if  os.getenv("PROD") != "true":

        uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
    else:
        uvicorn.run(app="main:app", host="0.0.0.0", port=80, reload=False)  # noqa: S104

if __name__ == "__main__":
    start_server()
