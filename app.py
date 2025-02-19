from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return 'Tejas is Hosting the Python App'
@app.route('/hi')
def hell():
    return '<h1>Hi from Flask & Docker</h1>'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
