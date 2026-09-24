from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def h():
    print("Hello, this is the git finnal test!")
    print("this is a confict merge")