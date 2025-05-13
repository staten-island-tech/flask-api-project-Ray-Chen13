from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = response.get("https://www.amiiboapi.com/api/amiibo/?name=mario")
    Mario_List = response.json()


    Mario = []

    for Mario in Mario_List:
        Mario.append({
            'amiiboSeries': Mario["amiiboSeries"].capitalize(),
            'character': Mario["character"]
        })

    return render_template("index.html", Mario = Mario)

@app.route("/pokemon/<int:id>")
def pokemon_detail(id):
    response = requests.get(f"https://www.amiiboapi.com/api/amiibo/?name=mario")
    Mario_List = response.json()
    for Mario in Mario_List:
        print(Mario)