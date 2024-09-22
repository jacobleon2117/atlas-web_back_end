#!/usr/bin/env python3
"""Session Authentication Views Module
"""
from flask import jsonify, abort, request
from models.user import User
from api.v1.views import app_views
from os import getenv


def login():
    """Log a user in and create a session.
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)
    response = jsonify(user[0].to_json())
    response.set_cookie(getenv('SESSION_NAME'), session_id)
    return response


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login_route():
    """Wrapper for the login function."""
    return login()


@app_views.route('/auth_session/logout/', methods=['DELETE'], strict_slashes=False)
def logout():
    """Log a user out by destroying the session.
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
