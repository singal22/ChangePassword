import flask
from flask import request
from pwdrequirements.ChangePassword import change_password

app = flask.Flask(__name__)


@app.route('/api/changepassword', methods=['GET'])
def api_filter():

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


app.run()
