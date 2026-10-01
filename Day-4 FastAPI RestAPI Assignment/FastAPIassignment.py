from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello {name}!"}

# Temporary data
items = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mobile", "price": 25000}
]


@app.get("/items")
def get_items():
    return items



# -------------------------
# GET - Get one item
# -------------------------
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item

    return {"message": "Item not found"}


# -------------------------
# POST - Create an item
# -------------------------
@app.post("/items")
def create_item(item: dict):
    items.append(item)

    return {
        "message": "Item created successfully",
        "item": item
    }


# -------------------------
# PUT - Replace/update an item
# -------------------------
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: dict):

    for item in items:
        if item["id"] == item_id:
            item.update(updated_item)

            return {
                "message": "Item updated successfully",
                "item": item
            }

    return {"message": "Item not found"}


# -------------------------
# PATCH - Partially update
# -------------------------
@app.patch("/items/{item_id}")
def patch_item(item_id: int, updated_data: dict):

    for item in items:
        if item["id"] == item_id:
            item.update(updated_data)

            return {
                "message": "Item partially updated",
                "item": item
            }

    return {"message": "Item not found"}


# -------------------------
# DELETE - Delete an item
# -------------------------
@app.delete("/items/{item_id}")
def delete_item(item_id: int):

    for item in items:
        if item["id"] == item_id:
            items.remove(item)

            return {
                "message": "Item deleted successfully"
            }

    return {"message": "Item not found"}