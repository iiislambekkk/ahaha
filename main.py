from flask import Flask, jsonify

app = Flask(__name__)

tutor = [
    {
        'title': 'Govno'
    },
    {
        'title': 'Govno'
    }
]

@app.route('/govno', methods=['GET'])
def get_list():
    return jsonify(tutor)

if __name__ == '__main__':
    app.run()