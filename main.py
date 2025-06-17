from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World v2"}


@app.get("/todos")
async def get_todos():
    return [
        {"id": 1, "detail": "first todos"},
        {"id": 2, "detail": "seconds todos"},
    ]


counter = 0


@app.get("/counter")
async def get_counter():
    global counter
    counter += 1
    return {"message": f"counter = {counter}"}


class Item(BaseModel):
    item_id: int
    name: str
    description: str | None = None
    price: float


class ItemDto(BaseModel):
    name: str
    description: str | None = None
    price: float


items: dict[int, Item] = {
    1 : Item(item_id=1, name="first item",price=10),
    2 : Item(item_id=2, name="second item",price=20),
    3 : Item(item_id=3, name="third item",price=30)
}
id = 0


@app.post("/items/", response_model=Item, tags=["items"])
def create_item(item: ItemDto):
    global id
    id += 1

    items[id] = Item(
        item_id=id, name=item.name, description=item.description, price=item.price
    )
    return items[id]

@app.get("/items", response_model=list[Item], tags=["items"])
def get_all_items():
    return [item for item in items.values()]

@app.get("/items/{item_id}", response_model=Item)
def get_one_items(item_id: int):
    return items[item_id]
