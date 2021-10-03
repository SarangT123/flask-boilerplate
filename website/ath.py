from website import views
from flask import Flask, Blueprint, request, render_template, redirect, session
import os
from dotenv import load_dotenv
load_dotenv()

ath = Blueprint('ath', __name__)


@ath.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return
    else:
        return


@ath.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return
    else:
        return


@ath.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        return
    else:
        return
