from flask_wtf import FlaskForm
import re
from wtforms import StringField, SubmitField
from wtforms.validators import Required, EqualTo, ValidationError


def lottery_check(form, field):
    p = re.compile(r'([0-9]|[1-5][0-9]|60)')
    if not p.match(form.field.data):
        raise ValidationError("All numbers must be between 1 and 60")


class lotteryForm(FlaskForm):
    no1 = StringField(validators=[Required(), lottery_check])
    no2 = StringField(validators=[Required(), lottery_check])
    no3 = StringField(validators=[Required(), lottery_check])
    no4 = StringField(validators=[Required(), lottery_check])
    n05 = StringField(validators=[Required(), lottery_check])
    no6 = StringField(validators=[Required(), lottery_check])
    submitDraw = SubmitField(validators=[Required()])
