from flask import Flask, jsonify, request

app = Flask(__name__)

players = []


@app.route('/circular', methods=['GET', 'POST'])
def circular_list():
    if request.method == 'POST':
        [players.append(player) for player in request.json]
        return jsonify(players), 201
    else:
        return jsonify(players)


@app.route('/circular/next')
def next_player():
    player = players.pop(0)
    players.append(player)
    return jsonify(players[0])


if __name__ == '__main__':
    app.run()
