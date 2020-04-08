from flask_restful import Resource, reqparse
from models.device import DeviceModel
from datetime import time

class Device(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('state',
        type = str,
        required = False,
    )
    parser.add_argument('nice_name',
        type = str,
        required = False,
    )
    # parser.add_argument('time',
    #     type = time(),
    #     required = False,
    # )
    parser.add_argument('sub_topic',
        type = str,
        required = False,
    )
    parser.add_argument('pub_topic',
        type = str,
        required = False,
    )

    def get(self, name):
        device = DeviceModel.find_by_name(name)
        if device:
            return device.json()
        return {'message': "Not Found: Device Could Not Be Found"}, 404

    def post(self, name):
        if DeviceModel.find_by_name(name):
            return {'message': f'Conflict: A device with name {name} already exists. '
            f'No two duplicate devices can be created.'}, 409

        data = Device.parser.parse_args()

        device = DeviceModel(name, data['sub_topic'], data['pub_topic'])

        device.save_to_db()
        return device.json(), 201

    def patch(self, name):
        device = DeviceModel.find_by_name(name)

        if device is None:
            return {'message': "Not Found: Device Could Not Be Found"}, 404

        data = Device.parser.parse_args()

        if data['state']:
            device.state = data['state']
        if data['nice_name']:
            device.nice_name = data['nice_name']
        if data['sub_topic']:
            device.sub_topic = data['sub_topic']
        if data['pub_topic']:
            device.pub_topic = data['pub_topic']
        device.save_to_db()
        return device.json()
