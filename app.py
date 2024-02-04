from flask import Flask,render_template,jsonify,request
import pickle
import sqlite3
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')