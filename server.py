from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from logic.tributeLogic import TributeLogic

app = Flask(__name__)
CORS(app)


@app.route('/api/tribute', methods=['POST'])
def add_new_tribute():
    try:
        tribute_json_object = request.json
        if tribute_json_object:
            TributeLogic.new_tribute(tribute_json_object)

    except Exception as exception_object:
        print(exception_object)
        return "Internal Server error", 500, {'ContentType': 'application/json'}

    return "", 200, {'ContentType': 'application/json'}


@app.route('/api/tributes/all')
def get_all_tributes():
    all_tributes = TributeLogic.get_all_tributes()
    return jsonify([tribute.json_format for tribute in all_tributes])


@app.route('/index.html')
def serve_index_page():
    return send_file('index.html')


@app.route('/add-tribute.html')
def serve_tribute_page():
    return send_file('add-tribute.html')


@app.route('/')
def home():
    return serve_index_page()


if __name__ == '__main__':
    app.run('127.0.0.1', 1967, True)
