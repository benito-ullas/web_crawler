from flask import Flask 
app = Flask(__name__)

@app.route('/')
def homepage():
    return """
    <h1>Hello world!</h1>

    <iframe src="https://storage.googleapis.com/winter-dynamics-311908/TQWQQI9RHC8O/st23_osananajimi-ga-zettai-ni-makenai-love-comedy-episode-8.1622643303.mp4" width="853" height="480" frameborder="0" allowfullscreen></iframe>
    """

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
