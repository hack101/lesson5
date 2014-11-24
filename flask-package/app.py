from flask import Flask, redirect, request, url_for, render_template
import json

# config
# server will reload on source changes, and provide a debugger for errors
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__) # consume the configuration above

@app.route('/')
def index():
    return render_template('index.html')

message_list = []

# This url handles both GET and POST, with different functionality
@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'GET':
        return json.dumps(message_list)  # Convert message_list to a json string
    if request.method == 'POST':
        # request.data contains the json data from client
        msg = json.loads(request.data)  # Convert the json string to a python dict
        message_list.append(msg)
        return json.dumps({"status_message": "ok-created"})  # Return something


if __name__ == "__main__":
    app.run()