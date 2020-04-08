from db import db
from datetime import time
from mqtt import topic, payload

class DeviceModel(db.Model):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(99), nullable=False)
    nice_name = db.Column(db.String(99))
    state = db.Column(db.String(99))
    time = db.Column(db.Time())
    sub_topic = db.Column(db.String(99))
    pub_topic = db.Column(db.String(99))

    def __init__(self, name, sub_topic, pub_topic):
        self.name = name
        self.state = "Off"
        self.time = time()
        self.sub_topic = sub_topic
        self.pub_topic = pub_topic

    def json(self):
        return {'name': self.name, 'nice_name': self.nice_name, 'state': self.state, 'time': str(self.time), 'sub_topic': self.sub_topic, 'pub_topic': self.pub_topic}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def change_state():
        pass
