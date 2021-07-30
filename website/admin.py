from flask import Flask, Blueprint , render_template , redirect ,url_for , request

views = Blueprint('views', __name__)

@views.route('/admin')
def admin_login():
    if request.method == 'POST':
        return
    else:
        return