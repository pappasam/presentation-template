import os
from flask import render_template

def render_template_function(blueprint_name):
    '''Return render_template function that
    renders templates for corresponding blueprint

    :param blueprint_name: name of a relevant blueprint
    '''
    def f(filename, **kwargs):
        filepath = os.path.join(blueprint_name, filename)
        return render_template(filepath, **kwargs)
    return f
