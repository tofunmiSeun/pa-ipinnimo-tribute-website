from flask import Flask, send_file
app = Flask(__name__)



@app.route('/index.html')
def serve_index_page():
    return send_file('index.html')

@app.route('/add-tribute.html')
def serve_tribute_page():
    return send_file('add-tribute.html')

@app.route('/')
def home():
    serve_index_page()

if __name__ == '__main__':
    app.run('127.0.0.1', 1967, True)
