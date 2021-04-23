from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    name = StringField('Название формулы', validators=[DataRequired()])
    section = StringField('Раздел', validators=[DataRequired()])
    definition = StringField('Формула в формате Latex', validators=[DataRequired()])
    submit = SubmitField('Отправить')
