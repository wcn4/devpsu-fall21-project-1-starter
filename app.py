from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json

# Use this file as the flask app source if selected
app = Flask(__name__)

# Enable CORS
CORS(app)

# Handle Routing for the app
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_name(name=None):
    #Takes in name, which by default is none, but is passed to hello.html
    return render_template('hello.html', name=name)

@app.route('/parks')
def read_users():

    # Read the parks.json file and store it as parks
    with open('parks.json', 'r') as f:
        parks = json.load(f)
    #Passes in the variable parks
    return render_template('parks.html', parks=parks)


# Add a route to a return a json response like an API
#####################################################

#Make a dictionary containing the alphabet
@app.route('/api')
def api():
    alphabetDict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #Use for loop to map letters to index.
    for i in range(len(alphabet)):
        alphabetDict[alphabet[i]] = i
    return jsonify(alphabetDict)

# If this file is executed, run the app
if __name__ == "__main__":
    app.run()
