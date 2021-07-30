from website import views
from flask import Flask , Blueprint , request , render_template ,redirect , session
import os
from dotenv import load_dotenv
load_dotenv()

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return
    else:
        return

@auth.route('/register', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return
    else:
        return

@auth.route('/logout', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return
    else:
        return
