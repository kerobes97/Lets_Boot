import numpy as np, os
from flask import app, request, Blueprint, render_template
import pickle
# from flask_app.models import db.User

bp = Blueprint('main', __name__)

# APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 
# MODEL_PATH = os.path.join(APP_ROOT, "model.pkl") 
model = pickle.load(open("model.pkl", 'rb'))

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/login')
def login():
    return render_template('create.html')

@bp.route('/trends')
def trends():
    #User.query
    return render_template('trends.html')

@bp.route('/trends/busan')
def busan():
    return render_template('t_busan.html')

@bp.route('/trends/recommend', methods=['GET', 'POST'])
def predict():
    features = [int(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    prediction = prediction[0]
    return render_template('recommend.html', prediction = prediction)

@bp.route('/post')
def post():
    return render_template('post.html')

if __name__ == "__main__":
    app.run(debug = True)