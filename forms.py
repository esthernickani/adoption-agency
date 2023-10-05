from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import DataRequired, URL, Optional, NumberRange, AnyOf

class PetForm(FlaskForm):
    """Form for adding a pet"""
    name = StringField("Pet Name", 
                       validators=[DataRequired()])
    species = SelectField("Species", choices=[('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')],
                          validators=[DataRequired(), AnyOf(values=['cat', 'dog', 'porcupine'])])
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message='Enter an age between 0 and 30')])
    notes = StringField("Notes")