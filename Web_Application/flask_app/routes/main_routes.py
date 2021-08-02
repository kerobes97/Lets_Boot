from flask import Blueprint, render_template
# from flask_app.models import db.User

bp = Blueprint('main', __name__,  template_folder='templates')

@bp.route('/')
def index():
    return render_template('index.html')
    # return "Welcome to Index page"

@bp.route('/login')
def login():
    return render_template('create.html')

@bp.route('/trends')
def trends():
    #User.query
    return render_template('trends.html')

@bp.route('/post')
def post():
    return render_template('post.html')