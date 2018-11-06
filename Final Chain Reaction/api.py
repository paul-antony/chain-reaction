from __future__ import print_function
from flask import Flask, request, jsonify, render_template
import sys

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def main():

    content = request.json
    print("hi", file=sys.stderr)

    return content

app.run()
