from flask import Flask, redirect, request
from db import items, stores
from flask_smorest import abort
import uuid


app = Flask(__name__)



@app.get("/")
def home():
    return redirect("/store")

@app.get("/store") # /store refers root or endpoint # http://127.0.0.1:5000/store
def get_stores():
    return {"stores" : list(stores.values())}

@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400, message="Bad request. Ensure 'name' is included in the JSON payload.")
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(400, message=f"{store} is already exist.")
    
    
    store_id = uuid.uuid4().hex
    store = {**store_data, "id" : store_id}
    stores[store_id] = store
    return store, 201

@app.post("/item")
def create_item():
    item_data = request.get_json() 
    if (
        "price" not in item_data
        or "store_id" not in item_data
        or "name" not in item_data
    ) :
        abort(
            400,
            message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload"
        )
    for item in items.values():
        if (
            item_data["name"] == item["name"] and
            item_data["store_id"] == item["store_id"]
        ):
            abort(400, message= f"{item} already exist")
    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")
           
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item, 201





@app.get("/item")
def get_all_items():
    return {"stores" : list(items.values())}    
    
@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found")

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found")



@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message" : "Item deleted."}
    except KeyError:
        abort(404, message="Item is not found")

@app.delete("/store/<string:store_id>")
def store(store_id):
    try:
        del stores[store_id]
        return {"message" : "Store deleted."}
    except KeyError:
        abort(404, message="Store is not found")


@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data =request.get_json()
    if "price" not in item_data or "name" not in item_data:
        abort(
            400,
            message="Bad request. Ensure 'price', and 'name' are included in the JSON payload.",
        )
    try:
        item = items[item_id]
        item |= item_data # new dictionary update operator, merge the two dictionaries.

        return item
    except KeyError:
        abort(404, message="Item not found.")