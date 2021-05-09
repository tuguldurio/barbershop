from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta

from api import blueprint as api1

app = Flask(__name__)

# CORS
cors = CORS(app, resources={r"/api/*": {'origins': ['http://localhost:8080','http://192.168.0.235:8080']}})
# app.config['PROPAGATE_EXCEPTIONS'] = True

# JWT
app.config["JWT_SECRET_KEY"] = 'very-very-secret'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)

# Routes
app.register_blueprint(api1)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8000, use_reloader=True)