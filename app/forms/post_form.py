from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length
from wtforms.widgets import TextArea

class PostForm(FlaskForm):
    body = StringField("Texto da postagem", validators=[DataRequired("Insira o texto da postagem!"), length(min=4, max=255, message="Texto curto ou longo demais")], widget=TextArea())
    submit = SubmitField("Postar")