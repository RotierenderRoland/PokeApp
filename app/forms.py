from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    pokemon = StringField('Pokemon name or ID', validators=[DataRequired()])
    submit = SubmitField('Submit')