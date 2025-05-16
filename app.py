from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://www.amiiboapi.com/api/amiibo/?name=mario")
    data = response.json()
    mario_list = data

    games = []

    for game in mario_list:
        games.append({
            'amiiboSeries': game['amiiboSeries'].capitalize(),
            'head': game['head'] 
        })

        return render_template("index_html", games = games)
    
@app.route("/pokemon/<int:id>")
def game_detail(id):
    response = requests.get("https://www.amiiboapi.com/api/amiibo/?name=mario")
    data = response.json()

    amiiboSeries = data.get('amiiboSeries').capitalize()
    character = data.get('character)').capitalize()
    head = data.get('head')
    name = data.get('name').capitalize()