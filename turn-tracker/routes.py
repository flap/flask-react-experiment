from flask import Flask, jsonify, request

app = Flask(__name__)

players = []


@app.route('/circular', methods=['GET', 'POST', 'DELETE'])
def circular_list():
    if request.method == 'POST':
        players.clear()
        [players.append(player) for player in request.json]
        return jsonify(players), 201
    elif request.method == 'GET':
        return jsonify(players)
    else:
        players.clear()
        return jsonify(players), 204


@app.route('/circular/next')
def next_player():
    player = players.pop(0)
    players.append(player)
    return jsonify(players[0])


if __name__ == '__main__':
    app.run()
