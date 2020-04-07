from flask import Flask
from flask_restful import Api
from flask_mqtt import Mqtt

from db import db
from mqtt import mqtt
from resources.device import Device

app = Flask(__name__)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.config['MQTT_BROKER_URL'] = '192.168.1.130'
app.config['MQRR_BROKER_PORT'] = 1883

mqtt.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Device, '/device/<string:name>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
