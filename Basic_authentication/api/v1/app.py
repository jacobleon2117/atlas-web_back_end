#!/usr/bin/env python3
"""
    Route module for the API
"""
import os
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS

auth = None
auth_type = os.getenv('AUTH_TYPE')
if auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.before_request
def before_request():
    """
        Function executed before each request to filter incoming requests.

        It checks if authentication is required for the request path.
        If authentication is required and not provided, it aborts the request
        with appropriate status codes:
        - 401 Unauthorized: if the authorization header is missing.
        - 403 Forbidden: if the current user cannot be determined.
    """
    if auth is None:
        return
    public_routes = ['/api/v1/status/',
                     '/api/v1/unauthorized/',
                     '/api/v1/forbidden/']

    if request.path not in public_routes:
        if auth.require_auth(request.path, public_routes):
            if auth.authorization_header(request) is None:
                abort(401)
            if auth.current_user(request) is None:
                abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """
        Handler for 404 Not Found errors.

        Returns a JSON response indicating
        that the requested resource was not found.
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
        Handler for 401 Unauthorized errors.

        Returns a JSON response indicating that
        the request requires user authentication.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
        Handler for 403 Forbidden errors.

        Returns a JSON response indicating
        that the server understands the request,
        but refuses to authorize it.
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
