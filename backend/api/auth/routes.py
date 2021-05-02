from flask_restx import Namespace, Resource
from flask_jwt_extended import (create_access_token)
from flask import request

api = Namespace('auth')

@api.route('/token')
class Login(Resource):
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        if email != 'admin@email' or password != 'test':
            return {'message': 'Wrong email or password!'}, 401

        access_token = create_access_token(identity=email)
        return {'access_token': access_token}