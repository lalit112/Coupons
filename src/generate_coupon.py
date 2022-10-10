"""
This module generates a coupon for a brand
"""

import random
import string
from flask import Blueprint, request, jsonify
from authentication.token_auth import token_required
from database.models import Coupon
from database.models import db

# creating a blueprint
generate_coupon = Blueprint("generate_coupon", __name__)


@generate_coupon.route('/generate_coupon', methods=['POST'])
@token_required
def generate():
    """
    Function to generate coupons
    :return: Json string
    """
    data = request.get_json().get('count')
    for i in range(0, int(data)):
        coupon_code = ''.join(random.choices(string.ascii_letters, k=16))
        insert_coupon = Coupon(coupon_id=str(coupon_code), brand='Jack&Jones', validity=30, used=False)
        db.session.add(insert_coupon)
        db.session.commit()
    return jsonify("Status: Coupons Inserted Successfully")
