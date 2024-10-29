from flask import jsonify, request, Blueprint
from .models import db, CakeBakery
from .models import Cake, Bakery
from .checks import (
    check_data_create_cake,
    check_data_update_cake,
    check_data_create_bakery,
    check_data_update_bakery
)

api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")

@api_v1.route("/cakes", methods=("GET", "POST"))
def cakes():
    if request.method == "GET":
        print("Received query params:", request.args)
        query = Cake.query

        if flavor := request.args.get("flavor"):
            query = query.filter_by(flavor=flavor)

        if price := request.args.get("price", type=float):
            query = query.filter_by(price=price)

        if page := request.args.get("page", type=int):
            per_page = request.args.get("limit", 10, type=int)
            pagination = query.paginate(page=page, per_page=per_page, error_out=True)
            objs = pagination.items
            return jsonify([obj.to_json() for obj in objs]), 200

        objs = query.all()
        return jsonify([obj.to_json() for obj in objs]), 200

    if request.method == "POST":
        data = request.get_json()
        check_result = check_data_create_cake(data)

        if check_result == "OK":
            obj = Cake(
                name=data["name"],
                flavor=data["flavor"],
                price=data["price"],
                available=data["available"]
            )
            db.session.add(obj)
            db.session.commit()

            return jsonify(obj.to_json()), 201

        else:
            return jsonify({ "error": check_result }), 400

@api_v1.route("/cakes/<int:cake_id>", methods=("GET", "PUT", "DELETE"))
def cake(cake_id: int):
    obj = Cake.query.filter_by(id=cake_id).first()
    if not obj:
        return {}, 404

    if request.method == "GET":
        return obj.to_json(), 200

    elif request.method == "PUT":
        data: dict = request.get_json()
        check_result: str = check_data_update_cake(data)

        if check_result == "OK":
            if data.get("name", None):
                obj.name = data["name"]
            if data.get("flavor", None):
                obj.flavor = data["flavor"]
            if data.get("price"):
                obj.price = data["price"]
            if data.get("available", None) is not None:
                obj.available = data["available"]

            return obj.to_json(), 200

        else:
            return {"error": check_result}, 400

    elif request.method == "DELETE":
        db.session.delete(obj)
        db.session.commit()

        return obj.to_json(), 204


@api_v1.route("/bakeries", methods=("GET", "POST"))
def bakeries():
    if request.method == "GET":
        objs = Bakery.query.all()
        return jsonify([obj.to_json() for obj in objs]), 200

    elif request.method == "POST":
        data = request.get_json()
        check_result = check_data_create_bakery(data)

        if check_result == "OK":
            obj = Bakery(
                name=data["name"],
                location=data["location"],
                rating=data["rating"]
            )
            db.session.add(obj)
            db.session.commit()

            return obj.to_json(), 201

        else:
            return {"error": check_result}, 400

@api_v1.route("/bakeries/<int:bakery_id>", methods=("GET", "PUT", "DELETE"))
def bakery(bakery_id: int):
    obj = Bakery.query.filter_by(id=bakery_id).first()
    if not obj:
        return {}, 404

    if request.method == "GET":
        return obj.to_json(), 200

    elif request.method == "PUT":
        data: dict = request.get_json()
        check_result: str = check_data_update_bakery(data)

        if check_result == "OK":
            if data.get("name", None):
                obj.name = data["name"]
            if data.get("location", None):
                obj.location = data["location"]
            if data.get("rating", None):
                obj.rating = data["rating"]

            return obj.to_json(), 200

        else:
            return {"error": check_result}, 400

    elif request.method == "DELETE":
        db.session.delete(obj)
        db.session.commit()
        return obj.to_json(), 204


@api_v1.route("/bakeries/<int:bakery_id>/cakes", methods=("GET",))
def get_cakes_by_bakery(bakery_id: int):
    if not Bakery.query.filter_by(id=bakery_id).first():
        return {"error": "Bakery was not found"}, 404

    cakes_obj = db.session.query(Cake).join(CakeBakery).filter(CakeBakery.bakery_id == bakery_id).all()

    return jsonify([obj.to_json() for obj in cakes_obj]), 200