from db import db
from datetime import datetime

class DeviceModel(db.Model):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    nice_name = db.Column(db.String(99), nullable=True)
    state = db.Column(db.String(99), nullable=True)
    time = db.Column(db.DateTime(), nullable=True)

    def __init__(self, name):
        self.name = name
        self.state = "Off"

    def json(self):
        return {'name': self.name, 'nice_name': self.nice_name, 'state': self.state, 'time': self.time}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
