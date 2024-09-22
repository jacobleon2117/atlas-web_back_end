#!/usr/bin/env python3
"""
    Route module for the API

    This module sets up the Flask application, handling various routes,
    authentication mechanisms, and error responses. It supports both
    basic and generic authentication, and integrates with CORS to
    enable cross-origin requests for specified routes.
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os

auth = None
auth_type = getenv('AUTH_TYPE')
if auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.before_request
def handle_request():
    """ handle request authorization
    """
    handled_paths = ['/api/v1/status/',
                     '/api/v1/unauthorized/',
                     '/api/v1/forbidden/',
                     '/api/v1/auth_session/login/']
    if auth is not None:
        request.current_user = auth.current_user(request)
        if auth.require_auth(request.path, handled_paths) is True:
            if (auth.authorization_header(request) is None
                    and auth.session_cookie(request) is None):
                abort(401)
            if request.current_user is None:
                abort(403)

@app.errorhandler(404)
def not_found(error) -> str:
    """
    Handles 404 Not Found errors.
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Handles 401 Unauthorized errors.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
        Forbidden route handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
