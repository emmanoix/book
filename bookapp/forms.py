from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf.file import FileField,FileAllowed,file_required

class SignupForm(FlaskForm):
    fullname = StringField("Fullname",validators=[DataRequired(message="your fullname is required")])
    email = StringField("Your Email",validators=[Email()])
    password = PasswordField("password", validators=[DataRequired()])
    confirm_password = PasswordField("confirm password", validators=[EqualTo('password',message='confirm password must be equal to password')])
    btn = SubmitField("sign up!")
 
class ProfileForm(FlaskForm): 
    fullname=StringField("Fullname",validators=[DataRequired(message="your fullname is required")])
    pix=FileField("Display picture",validators=[file_required(),FileAllowed(['jpg','png'],'images only!')])
    btn = SubmitField("update profile")
    
    
    
     
    

