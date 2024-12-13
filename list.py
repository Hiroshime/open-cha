from flask import Flask
from models import db
from basic_views import basic_views

app = Flask(__name__)
app.config.from_pyfile('./config.py')
app.register_blueprint(basic_views)
db.init_app(app)

with app.test_request_context():

     db.create_all()

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run(debug=True)