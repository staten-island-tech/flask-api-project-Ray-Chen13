from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = response.get("https://amiiboapi.com/")
    data = response.json()
    Mario_List = data['results']

    Mario = []

    for Mario in Mario_List: