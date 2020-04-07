from flask import Flask
from flask_restful import Api

from db import db
from resources.device import Device

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Device, '/device/<string:name>')

if __name__ == '__main__':
    app.run(port=8080, debug=True)