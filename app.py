from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the homepage!'

@app.route('/get_image')
def get_image():
    return send_from_directory('static/upload', 'example.jpg')

if __name__ == '__main__':
    app.run(debug=True)
