from flask import Blueprint, jsonify, request
import sqlite3
import random

register = Blueprint("register", __name__)
connection = sqlite3.connect("../database/db.db", check_same_thread=False)
c = connection.cursor()

@register.route("/register", methods=["POST"])
def register_page():
    data = request.args

    c.execute("SELECT * FROM users WHERE username=? AND email=?", (data["username"], data["email"]))
    first_result = c.fetchone()
    if first_result is not None:
        return jsonify({"operation status": "failed", "message":"someone is already using this username/email"})

    user_id = str(random.getrandbits(128))
    c.execute("INSERT INTO users(username, password, email, user_id) VALUES(?, ?, ?, ?)", (data["username"], data["password"], data["email"], user_id));
    connection.commit()
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id, ))
    info = c.fetchone()
    return jsonify({"operation status": "success", "username": data["username"], "email": data["email"], "createdAt":info[3], "updatedAt":info[4], "user_id": info[5], "password": info[2]})