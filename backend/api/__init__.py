from flask import Blueprint
from flask_restx import Api
from .booking.routes import api as ns1
from .auth.routes import api as ns2
# from flask_cors import CORS

blueprint = Blueprint('api', __name__, url_prefix='/api')
# CORS(blueprint, resources={r"/api/*": {'origins': ['http://localhost:8080','http://192.168.0.235:8080']}}) 
api = Api(blueprint,
    title='Barber API',
    version='1.0',
    description='API for barber service',
    # All API metadatas
)

api.add_namespace(ns1)
api.add_namespace(ns2)