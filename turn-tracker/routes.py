from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/circular', methods=['GET', 'POST'])
def circular_list():
    if request.method == 'POST':
        players = []
        [players.append(player) for player in request.json]
        return jsonify(players)
    else:
        # You probably don't have args at this route with GET
        # method, but if you do, you can access them like so:
        # yourarg = flask.request.args.get('argname')
        # your_register_template_rendering(yourarg)
        return jsonify('Hello, World!')


if __name__ == '__main__':
    app.run()
