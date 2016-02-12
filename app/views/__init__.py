from flask import Blueprint, render_template
from .course1 import course1

index_bp = Blueprint("index", __name__)

@index_bp.route("/")
def index():
    return render_template('index.html')

views = [
        course1,
        index_bp,
        ]
