from flask import Blueprint, request, jsonify
import sqlite3
import re
import datetime

getusers = Blueprint("getusers", __name__)
connection = sqlite3.connect("../database/db.db", check_same_thread=False)
c = connection.cursor()

@getusers.route("/getusers", methods=["GET"])
def getusers_page():

    def isValidDate(array: list) -> bool:
        return datetime.datetime.strptime(f"{array[0]}-{array[1]}-{array[2]}", "%Y-%m-%d") > datetime.datetime.now()

    data = request.args
    if not re.search("^\d{4}-\d{2}-\d{2}$", data["start_date"]) or not re.search("^\d{4}-\d{2}-\d{2}$", data["end_date"]):
        return jsonify({
            "operation status": "failed",
            "message": "wrong date format (YYYY-MM-DD)"
        })

    c.execute("SELECT * FROM users WHERE createdAt BETWEEN ? AND ?", (data["start_date"], data["end_date"]))
    result = c.fetchone()
    if result is None:
        return jsonify({})
    
    return jsonify({
        "username": result[0],
        "lastLogin": result[4],
        "createdAt": result[5],
        "updatedAt": result[6]
    })