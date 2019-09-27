#
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError



class PitchForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("write your pitch here?",validators=[Required()])
	category = RadioField('Label', choices =[ ('love','love'),('product','product'),('motivation','motivation')],validators=[Required()])
	submit = SubmitField('Submit')
