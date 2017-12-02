from flask import Flask, send_file
app = Flask(__name__)


@app.route('/')
def serve_index_page():
    return send_file('index.html')

if __name__ == '__main__':
    app.run('127.0.0.1', 1967, True)
