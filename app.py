from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def h():
    print("Hello, this is the git finnal test!")
    
    print("this is a confict test from feature/chat")
    
    print("test push again")

    print("this is a merge confict caused by rag branch")
    print("test pull request")
    print("test push")


    print("this is a merge confict, and successful finished")

    print("use stash to record the code...")

    print("constuct a pull request")

