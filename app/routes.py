from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

#starting page
@bp.route('/', methods = ['GET'])
def index():
    return(render_template('index.html'))

@bp.route('/main_menu', methods = ['GET'])
def main_menu():
    return(render_template('main_menu.html'))