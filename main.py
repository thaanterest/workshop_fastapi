from fastapi import FastAPI 

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/todos")
async def get_todos():
    return [
        {"id" : 1, "detail": "first todos"},
        {"id" : 2, "detail": "Seconds todos"},
        {"id" : 3, "detail": "Third todos"}
    ]


counter = 0
@app.get("/counter")
async def get_counter():
    global counter
    counter += 1
    return {"message": f"Counter is {counter}"}
