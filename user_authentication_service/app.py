#!/usr/bin/env python3
"""
    flask - module
"""

from flask import Flask, jsonify, abort, request, redirect
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
        base route
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    """
        registration route
    """
    email = request.form['email']
    password = request.form['password']
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
        login route
    """
    email = request.form['email']
    password = request.form['password']
    if AUTH.valid_login(email, password):
        AUTH.create_session(email)
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
        logout route
    """
    session = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/', 302)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """
        profile route
    """
    user_session = request.cookies.get('session_id')
    if user_session is None:
        abort(403)
    user = AUTH.get_user_from_session_id(user_session)
    if user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """
        reset route
    """
    email = request.form['email']
    try:
        reset = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset})
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """
        update route
    """
    email = request.form['email']
    new_password = request.form['new_password']
    reset_token = request.form['reset_token']
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"})
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
