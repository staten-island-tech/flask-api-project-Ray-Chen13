from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://www.amiiboapi.com/api/amiibo/?name=mario")
    data = response.json()
    marios = []

    for mario in data.get('amiibo', []):
        marios.append({
            'series': mario['amiiboSeries'],
            'character': mario['character'],
            'id': mario['head'] + mario['tail'],  # Construct unique ID
            'image': mario.get('image')
        })

    return render_template("index.html", marios=marios)

@app.route("/mario/<mario_id>")
def mario_detail(mario_id):
    response = requests.get("https://www.amiiboapi.com/api/amiibo/?name=mario")
    data = response.json()

    selected = None
    for mario in data.get('amiibo', []):
        id = mario['head'] + mario['tail']
        if id == mario_id:
            selected = mario
            break

    if selected:
        return render_template("detail.html", mario=selected)
    else:
        return "Mario not found", 404

if __name__ == '__main__':
    app.run(debug=True)
