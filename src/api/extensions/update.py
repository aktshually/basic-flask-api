from flask import Blueprint, jsonify, request
import sqlite3

update = Blueprint("update", __name__)
connection = sqlite3.connect("../database/db.db", check_same_thread=False)
c = connection.cursor()

@update.route("/update", methods=["PUT"])
def update_page():
    data = request.args
    types = {
        "password": 2,
        "username": 0,
        "email": 1
    }
    possible = [x for x in types.keys()]
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (data["email"], data["password"]))
    result = c.fetchone()
    if result is None:
        return jsonify({
            "operation status": "failed",
            "message":"email or password are incorrect"
        })
    
    if not data["item_to_update"] in possible:
        return jsonify({
            "operation status": "failed",
            "message": "You can not change this info"
        })
    
    if data["old_info"] != result[types[data["item_to_update"]]]:
        return jsonify({
            "operation status": "failed",
            "message": "old info do not match with the real old info"
        })
    
    c.execute(f"UPDATE users SET {data['item_to_update']}=?, updatedAt=(DATETIME('now', '-3 hour')) WHERE user_id=?", (data["new_info"], result[3]))
    connection.commit()
    return jsonify({
        "operation status": "success",
        "message": "Information was changed successfully!"
    })