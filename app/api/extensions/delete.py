from flask import Blueprint, request, jsonify
import sqlite3

delete = Blueprint("delete", __name__)
connection = sqlite3.connect("../database/db.db", check_same_thread=False)
c = connection.cursor()

@delete.route("/delete", methods=["DELETE"])
def delete_page():
    queries = request.args
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (queries["email"], queries["password"]))
    result = c.fetchone()
    if result is None:
        return jsonify({
            "operation status": "failed",
            "message": "password/email do not match",
            "items": [queries["email"], queries["password"]]
        })
    
    c.execute("DELETE FROM users WHERE user_id=?", (result[5], ))
    connection.commit()
    return jsonify({
        "operation status": "success",
        "message": "Your account has been deleted successfully"
    })