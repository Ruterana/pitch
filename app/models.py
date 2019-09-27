from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    pass_secure = db.Column(db.String(255))
    email= db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String())
    pitches = db.relationship('Pitch',backref = 'users',lazy="dynamic")
    @property
    def password(self):
         raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    @login_manager.user_loader
    def load_user(user_id):
       return User.query.get(int(user_id))

class Pitch(db.Model):
    __tablename__ = 'pitches'
    pitch_id = db.Column(db.Integer,primary_key = True)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    upvote = db.Column(db.String(255))
    downvote = db.Column(db.String(255))
    title =db.Column(db.String(255))
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    category = db.Column(db.String(255), nullable=False)
    
    @classmethod
    def get_pitches(cls,id):
        pitch = Pitch.query.filter_by(pitch_id=pitch_id).all()
        return pitch
    def __repr__(self):
        return f'pitch{self.description}'


