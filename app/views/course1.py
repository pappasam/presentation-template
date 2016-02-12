from flask import Blueprint
from .utils import render_template_function

#######################################################################
# Initialize Blueprint
#######################################################################
NAME = "course1"
course1 = Blueprint(NAME, __name__, url_prefix="/" + NAME)
render_template = render_template_function(NAME)

#######################################################################
# Create views
#######################################################################
@course1.route("/session1")
def session1():
    return render_template('session1.md')

@course1.route("/session2")
def session2():
    return render_template('session2.md')
