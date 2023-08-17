#!/usr/bin/env python3
"""Basic flask appliction"""


from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


app = Flask(__name__)
Auth = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """implementing the user registration"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = Auth.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": f"{email}", "message": "user created"})


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """implementing the user login"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not Auth.valid_login(email, password):
        abort(401)
    session_id = Auth.create_session(email)
    resp = jsonify({"email": f"{email}", "message": "logged in"})
    resp.set_cookie('session_id', session_id)
    return resp


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    session_id = request.cookies.get('session_id', None)
    user = Auth.get_user_from_session_id(session_id)

    if user is None:
        abort(403)
    Auth.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """getting the user profile"""
    session_id = request.cookies.get('session_id')
    user = Auth.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
