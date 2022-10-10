"""
Module for generating access token
"""

import jwt
from flask import request, make_response, Blueprint, jsonify
from flask import current_app as app
from database.models import Customer, db

authenticate = Blueprint("authenticate", __name__)


@authenticate.route('/', methods=['POST'])
def generate_token():
    """
    Function to generate token for authentication
    :return: token
    """
    auth = request.get_json()
    if not auth:
        return make_response('Could not found parameter id in request', 401,
                             {'WWW-Authenticate': 'Basic-realm= "Pass id as parameter in request body"'})
    user = db.session.query(Customer.customer_id).filter(Customer.customer_id == auth['id']).first()
    if not user:
        return make_response('Could not verify user', 401, {'WWW-Authenticate': 'Basic-realm= "No user found!"'})
    token = jwt.encode({'id': user.customer_id}, app.config['SECRET_KEY'], 'HS256')
    return make_response(jsonify({'token': token}), 201)
