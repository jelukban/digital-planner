from flask import Flask, render_template, request, flash, redirect, jsonify
from model import connect_to_db, db
import json

app = Flask(__name__)
app.secret_key = "dev"

if __name__ == "__main__":

    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
