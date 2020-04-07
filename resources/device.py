from flask_restful import Resource, reqparse

from models.device import DeviceModel

class Device(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('state',
        type = str,
        required = False,
    )

    def get(self, name):
        device = DeviceModel.find_by_name(name)
        if device:
            return device.json()
        else:
            return {'message': "Item not found"}, 400

    def post(self, name):
        if DeviceModel.find_by_name(name):
            return {'message': f'An item with name {name} already exists'}, 400

        data = Device.parser.parse_args()

        device = DeviceModel(name)
        device.save_to_db()
        return device.json(), 201

    def put(self, name):
        data = Device.parser.parse_args()
        device = DeviceModel.find_by_name(name)

        if device is None:
            return {'message': "Device doesn't exist."}, 400
        else:
            device.state = data['state']
            device.save_to_db()
            return device.json(), 201
