from flask import Flask, jsonify, request
from collections import deque

app = Flask(__name__)

players = []


@app.route('/circular', methods=['GET', 'POST'])
def circular_list():
    if request.method == 'POST':
        [players.append(player) for player in request.json]
        return jsonify(players), 201
    else:
        # You probably don't have args at this route with GET
        # method, but if you do, you can access them like so:
        # yourarg = flask.request.args.get('argname')
        # your_register_template_rendering(yourarg)
        return jsonify('Hello, World!')


@app.route('/circular/next')
def next_player():
    player = players.pop(0)
    players.append(player)
    return jsonify(players[0])


if __name__ == '__main__':
    app.run()
