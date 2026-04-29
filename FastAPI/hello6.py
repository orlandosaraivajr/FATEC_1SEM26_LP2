from fastapi import FastAPI, Header

app = FastAPI()

@app.post("/hi")
def greet(who:str = Header()):
    return f"Hello? {who}?"


@app.post("/agent")
def get_agent(user_agent:str = Header()):
    return user_agent


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello6:app", reload=True)