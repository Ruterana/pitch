from flask import render_template,request,redirect,url_for,abort
from ..models import User,Pitch
from . import main
from .forms import PitchForm
from .. import db,photos
from flask_login import login_required,current_user
import markdown2 

@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    pitch = Pitch.query.all()
    title = 'Welcome Home-Minute Pitch'
    love = Pitch.query.filter_by(category="love")
    product = Pitch.query.filter_by(category = "product")
    motivation = Pitch.query.filter_by(category = "motivation")
    
    return render_template('index.html', title = title, pitch = pitch, love=love, product= product, motivation = motivation)




    return render_template('index.html',title = title)
@main.route('/pitch/new',methods=['GET','POST'])
@login_required
def new_pitch():
    form= PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        category= form.category.data
        new_pitch = Pitch(user_id =current_user._get_current_object().id, title = title,description=description,category=category)
        db.session.add(new_pitch)
        db.session.commit()
        return redirect (url_for('main.index'))
    return render_template('pitch.html',pitch_form=form)
