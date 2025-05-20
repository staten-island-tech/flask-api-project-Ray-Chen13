from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://www.amiiboapi.com/api/amiibo/?name=mario")
    data = response.json()
    mario_list = data['amiibo']

    games = []

    for game in mario_list:
        games.append({
            'amiiboSeries': game['amiiboSeries'].capitalize(),
            'head': game['head'],
            'tail': game['tail'],
        })

    return render_template("index.html", games=games)
    
@app.route("/pokemon/<int:id>")
def game_detail(head):  
    response = requests.get("https://www.amiiboapi.com/api/amiibo/?name=mario")
    data = response.json()

    amiiboSeries = data.get('amiiboSeries').capitalize()
    character = data.get('character)').capitalize()
    name = data.get('name').capitalize()
    tail = data.get('tail')
    image_url = f"https://raw.githubusercontent.com/N3evin/AmiiboAPI/master/images/icon_{head}-{tail}.png"
    image = image_url

    return render_template("mario.html", mario={
        'amiiboSeries': amiiboSeries,
        'character': character,
        'image': image_url,
        'name': name, 
        'tail': tail
    })
if __name__ == '__main__':
    app.run(debug=True)