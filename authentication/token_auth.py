"""
This module verifies the token
"""
import os
from functools import wraps
import jwt
from flask import request, jsonify, make_response
from database.models import Customer
from dotenv import load_dotenv

load_dotenv()


def token_required(f):
    """
    Act as decorator on functions for checking the required access
    :param f: function
    :return: decorated function
    """

    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        # ensure the jwt-token is passed with the headers
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:  # throw error if no token provided
            return make_response(jsonify({"message": "A valid token is missing!"}), 401)
        try:
            # decode the token to obtain user public_id
            data = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=['HS256'])
            current_user = Customer.query.filter(Customer.customer_id == data['id']).first()
        except:
            return make_response(jsonify({"message": "Invalid token!"}), 401)
        # Return the user information attached to the token
        return f(current_user, *args, **kwargs)

    return decorator
