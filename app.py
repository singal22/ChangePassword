import flask
import json
from flask import request
from pwdrequirements.ChangePassword import change_password

app = flask.Flask(__name__)


@app.route('/api/changepassword', methods=['GET'])
def api_get():

    if not request.args:
        return "Old and new password are missing in parameters"

    query_parameters = request.args

    if query_parameters.get('old_password'):
        old = query_parameters.get('old_password')
    else:
        return "Old password parameter is missing"

    if query_parameters.get('new_password'):
        new = query_parameters.get('new_password')
    else:
        return "New password parameter is missing"

    if change_password(old, new):
        return "Password can be successfully changed"
    else:
        return "Password cannot be changed !!"


@app.route('/api/changepassword', methods=['POST'])
def api_post():

    data = request.json
    if not data:
        return "Old and new password are missing in parameters"

    if data['old_password']:
        old = data['old_password']
    else:
        return "Old password is missing"

    if data['new_password']:
        new = data['new_password']
    else:
        return "New password is missing"

    if change_password(old, new):
        return "Password can be successfully changed"
    else:
        return "Password cannot be changed !!"


app.run(host='0.0.0.0')
