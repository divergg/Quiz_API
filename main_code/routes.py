from main_code import app
from flask_restful import Resource, Api, reqparse
from .models import Record
from blinker import signal
from flask import jsonify
from .side_api_request import make_request, handle_post_request


api = Api(app)

"""A parser for requests to our API"""
parser = reqparse.RequestParser()
parser.add_argument('questions_num', required=True, type=int)

"""A signal, that is activated when a post request to API is made"""
post_request_signal = signal('post-request-signal')
post_request_signal.connect(handle_post_request, app)


class ApiTest(Resource):

    def get(self):
        records = Record.query.all()
        rec_json = [rec.to_json() for rec in records]
        return rec_json

    def post(self):
        args = parser.parse_args()
        count = args['questions_num']
        last_record = Record.query.order_by(Record.date.desc()).first()
        post_request_signal.send(app, count=count)

        if last_record:
            # Convert the last instance to a JSON object
            json_data = last_record.to_json()
        else:
            json_data = []

        return jsonify({'message': 'Success', 'data': json_data})


api.add_resource(ApiTest, '/')



