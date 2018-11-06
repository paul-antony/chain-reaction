from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

log_file = None

@app.route('/', methods=['GET', 'POST'])
def game():
    if request.method == 'GET':
        if log_file is not None:
            return "Log file not instantiated yet", 404
        else:
            return jsonify(log_file)
    elif request.method == 'POST':
        log_file = request.form
        if log_file is not None:
            return "Ok"
        else:
            return "No data provided", 400

app.run()
