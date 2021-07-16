from flask import Blueprint, request, jsonify
import sqlite3

login = Blueprint("login", __name__)
connection = sqlite3.connect("../database/db.db", check_same_thread=False)
c = connection.cursor()

@login.route("/login", methods=["GET"])
def login_page():
    data = request.args
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (data["username"], data["password"]))
    result = c.fetchone()
    if result is None:
        return jsonify({"status": "username or password are incorrect"})

    c.execute("UPDATE users SET lastLogin=datetime('now', '-3 hour') WHERE user_id=?", (result[3], ))
    connection.commit()

    return jsonify(
        {
            "status": "logged sucessfully",
            "data": {
                "username": result[0],
                "email": result[1],
                "user_id": result[3],
                "lastLogin": result[4],
                "createdAt": result[5],
                "updatedAt": result[6]
            }
        }
    )