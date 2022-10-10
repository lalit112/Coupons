"""
This module fetches available coupons on demand for customers
"""

from flask import Blueprint, request, jsonify

from authentication.token_auth import token_required
from database.models import db
from database.models import Customer, Coupon

# creating blueprint
fetch_coupon = Blueprint("fetch_coupon", __name__)


@fetch_coupon.route('/', methods=["GET"])
@token_required
def get_coupon():
    """
    Function for fetching coupons
    :return: json string
    """
    coupon = db.session.query(Coupon.coupon_id).filter(Coupon.used == False).first()
    customer_id = request.get_json().get("userid")
    name = request.get_json().get("name")
    address = request.get_json().get("address")
    Coupon.query.filter(Coupon.coupon_id == coupon[0]).update(dict(used=True))
    insert_customer_data = Customer(customer_id=customer_id, coupon=coupon[0], name=name, address=address)
    db.session.add(insert_customer_data)
    db.session.commit()
    return jsonify(f"Coupon:{coupon} assigned to customer with customerid {customer_id}")
