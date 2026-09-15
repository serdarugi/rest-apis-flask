from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import jwt_required

from db import db
from models import StoreModel
from schemas import StoreSchema


blp = Blueprint("Stores", __name__, description="Operations on stores")


@blp.route("/store/<int:store_id>")
class Store(MethodView):
    @jwt_required()
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store
    @jwt_required()
    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleted"}


@blp.route("/store")
class StoreList(MethodView):
    @jwt_required()
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()

    @jwt_required()
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A store with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the store.")

        return store




# import uuid
# from flask import Flask, request
# from flask_smorest import Blueprint, abort
# from flask.views import MethodView
# from sqlalchemy.exc import IntegrityError,SQLAlchemyError

# from schemas import StoreSchema,PlainStoreSchema
# from models import StoreModel
# from db import db


# blp = Blueprint("Stores", __name__, description="Operations on stores")

# # /store operations with <string:store_id>
# @blp.route("/store/<string:store_id>")
# class Store(MethodView):
#     @blp.response(200,StoreSchema)
#     def get(self,store_id):
#         # try:
#         #     return stores[store_id]
#         # except KeyError:
#         #     abort(404,message="Store is not found")
#         store = StoreModel.query.get_or_404(store_id)
#         return store
    
#     def delete(self,store_id):
#         # try: 
#         #     del stores[store_id]
#         #     return {"message":"Store is deleted"}
#         # except KeyError:
#         #     abort(404,message="Store is not found")
#         store = StoreModel.query.get_or_404(store_id)
#         db.session.delete(store)
#         db.session.commit()
#         return {"message" : "Store deleted"}


# # /store operations without store_id     
# @blp.route("/store")
# class StoreList(MethodView):
#     @blp.response(200,StoreSchema(many=True))
#     def get(self):
#         return StoreModel.query.all()
    
#     @blp.arguments(PlainStoreSchema)
#     @blp.response(201,PlainStoreSchema)
#     def post(self,store_data):
#         #store_data = request.get_json()
#         # if "name" not in store_data:
#         #     abort(400,message="Bad Request. Ensure that JSON Payload includes 'name'")
#         # for store in stores.values():
#         #     if store_data["name"]==store["name"]:
#         #         abort(404,message=f"{store} already exists")
        
#         # store_id = uuid.uuid4().hex
#         # store = {**store_data, "id":store_id}
#         # stores[store_id] = store
#         # return store
#         store = StoreModel(**store_data)
#         try:
#             db.session.add(store)
#             db.session.commit()
#         except IntegrityError:
#             abort(400,message="A store already exists with that name")
#         except SQLAlchemyError:
#             abort(500,message="An error occured while creating the store")
#         return store