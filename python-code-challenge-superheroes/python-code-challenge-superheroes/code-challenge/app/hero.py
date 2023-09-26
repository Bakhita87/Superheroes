import datetime
from xmlrpc.client import DateTime
import db


class Hero(db.Model):
    _tablename_ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256),nullable = False)
    super_name = db.Column(db.String)
    created_at = db.Column(DateTime, default = datetime.utcnow)
    updated_at = db.Column(DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

    powers = db.relationship('Power', secondary='heroPowers', back_populates='heroes')

    def _init_(self, name, super_name):
        self.name = name  
        self.super_name = super_name  

    def _repr_(self):
        return f'<Hero(name={self.name}, super_name={self.super_name})>'
