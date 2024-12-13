from flask import request, session, Blueprint, redirect, url_for, render_template
from datetime import datetime
import os


from models import User, Gift, db

basic_views = Blueprint('basic_views',__name__,template_folder='templates')

@basic_views.route('/')
def index():
    return redirect(url_for('basic_views.login'))

@basic_views.route('/login')
def login():
    return render_template('login.html')

@basic_views.route('/authenticate', methods=['POST'])
def authenticate():
    while True:
        if request.form['name'] == os.getenv('ADMIN_NAME'):
            session['logged'] = os.getenv('ADMIN_ID')
            session['name'] = request.form['name']
            return redirect(url_for('basic_views.adm_gifts'))

        user = User.query.filter_by(name=request.form['name']).first()
        if user:
            session['logged'] = user.id
            session['name'] = user.name
            return redirect(url_for('basic_views.list_gift'))
        else:
            new_user = User(name=request.form['name'],register_date=datetime.now())
            db.session.add(new_user)
            db.session.commit()


@basic_views.route('/list_gift')
def list_gift():
    gifts = Gift.query.all()
    print(gifts)
    return render_template('giftlist.html',gifts=gifts)

@basic_views.route('/get_gift/<int:id>')
def get_gift(id):
    gift = Gift.query.get(id)

    if gift:
        gift.available = 0
        gift.user_id = session['logged']

        db.session.commit()

    return redirect(url_for('basic_views.list_gift'))

@basic_views.route('/release_gift/<int:id>')
def release_gift(id):
    gift = Gift.query.get(id)

    if gift:
        gift.available = 1
        gift.user_id = 0

        db.session.commit()

    return redirect(url_for('basic_views.list_gift'))

@basic_views.route('/adm_gifts')
def adm_gifts():
    if session['logged'] == os.getenv('ADMIN_ID'):
        gifts = Gift.query.all()
        print(gifts)
        return render_template('adminstrator.html',gifts=gifts)
    else:
        return redirect('basic_views.login')
@basic_views.route('/delete_gift/<int:id>')
def delete_gift(id):
    gift = Gift.query.get(id)

    if gift:
        db.session.delete(gift)
        db.session.commit()

    return redirect(url_for('basic_views.adm_gifts'))

@basic_views.route('/add_gift',methods=['POST'])
def add_gift():
    gift = Gift.query.filter_by(name=request.form['giftname']).first()

    if gift:
        return redirect(url_for('basic_views.adm_gifts'))
    else:
        new_gift = Gift(name=request.form['giftname'])
        db.session.add(new_gift)
        db.session.commit()
        return redirect(url_for('basic_views.adm_gifts'))