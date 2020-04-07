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
        return {'message': "Bad Request: Device Could Not Be Found"}, 400

    def post(self, name):
        if DeviceModel.find_by_name(name):
            return {'message': f'Bad Request: A device with name {name} already exists. '
            f'No two duplicate devices can be created.'}, 400

        device = DeviceModel(name)
        device.save_to_db()
        return device.json(), 201

    def put(self, name):
        data = Device.parser.parse_args()
        device = DeviceModel.find_by_name(name)

        if device is None:
            device = DeviceModel(name)
            device.save_to_db()
            return device.json(), 201
        else:
            device.state = data['state']
            device.save_to_db()
            return device.json(), 201
