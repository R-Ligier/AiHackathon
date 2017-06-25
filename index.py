
from flask import Blueprint, render_template, request, session, redirect

index = Blueprint("index", __name__, template_folder="templates", static_folder="static")

@index.route("/", methods=['GET', 'POST'])
def _index():
    return '0' 

