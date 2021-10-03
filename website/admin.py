from flask import Flask, Blueprint, render_template, redirect, url_for, request

admin = Blueprint('admin', __name__)


@admin.route('/admin')
def admin_login():
    if request.method == 'POST':
        return
    else:
        return
