import datetime
from flask import Flask, jsonify, request, send_file
from flask_jwt_extended import (JWTManager, create_access_token, get_jwt_identity, jwt_required)
from flask_cors import CORS

from handler.user_handler import find_user_by_username_and_password

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=24)
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)


@app.route('/login', methods=['POST'])
def login():
    try:
        params = request.get_json()
        username = params['username']
        password = params['password']
    except Exception as ex:
        print(ex)
        return jsonify(status='ERROR', message='داده ارسالی اشتباه است'), 400

    response = find_user_by_username_and_password(username, password)
    access_token = create_access_token(identity=username)

    if response.get('status') == 'OK':
        response['token'] = access_token
        return jsonify(response), 200

    return jsonify(response), 403


if __name__ == '__main__':
    app.run()