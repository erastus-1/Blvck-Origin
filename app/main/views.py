from flask import render_template, request, redirect, url_for,abort
from app.main import main
from flask_login import login_required, current_user
from .. import db,photos
from app.models import User, ProfilePhoto
from .forms import UpdateProfile

@main.route('/')
def index():

    title = 'Welcome to black origin'
    return render_template('index.html', title = title)

@main.route('/contacts')
def contact():
       
    title = 'Black origin Contacts'
    return render_template('contacts.html', title = title)

@main.route('/about')
def about():
       
    title = 'Black origin about page'
    return render_template('about.html', title = title)


@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("index.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.index',uname=uname))

