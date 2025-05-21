from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Fetch the data from the API
    response = requests.get("https://www.amiiboapi.com/api/amiibo/?name=mario")
    data = response.json()
    mario_list = data['amiibo']

    games = []
    for i, game in enumerate(mario_list):
        head = game['head']
        tail = game['tail']
        image_url = f"https://raw.githubusercontent.com/N3evin/AmiiboAPI/master/images/icon_{head}-{tail}.png"

        games.append({
            'id': i,
            'name': game['name'],
            'image': image_url
        })

    return render_template("index.html", games=games)

@app.route("/pokemon/<int:id>")
def game_detail(id):
    response = requests.get("https://www.amiiboapi.com/api/amiibo/?name=mario")
    data = response.json()
    game = data['amiibo'][id]

    image_url = f"https://raw.githubusercontent.com/N3evin/AmiiboAPI/master/images/icon_{game['head']}-{game['tail']}.png"

    release_dates = {
        'NA': game['release'].get('na', "N/A"),
        'EU': game['release'].get('eu', "N/A"),
        'JP': game['release'].get('jp', "N/A"),
        'AU': game['release'].get('au', "N/A"),
    }

    return render_template("mario.html", game=game, image_url=image_url, release_dates=release_dates)

if __name__ == '__main__':
    app.run(debug=True)
