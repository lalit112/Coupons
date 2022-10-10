"""
This module contains models for database
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Coupon(db.Model):
    """
    Coupon model class for storing coupon information
    """
    coupon_id = db.Column(db.String, primary_key=True)
    brand = db.Column(db.String(20), unique=False, nullable=False)
    validity = db.Column(db.Integer, unique=False, nullable=False)
    used = db.Column(db.Boolean, nullable=False)
    customer = db.relationship('Customer', backref='customer', lazy=True)

    # repr method represents how one object of this data table
    # will look like
    def __repr__(self):
        return f"Coupon_id : {self.coupon_id}, Brand: {self.brand}"


class Customer(db.Model):
    """
    Customer model class for storing customer related information
    """
    customer_id = db.Column(db.Integer, primary_key=True)
    coupon = db.Column(db.ForeignKey("coupon.coupon_id"))
    name = db.Column(db.String(80))
    address = db.Column(db.String(180))
