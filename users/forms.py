from flask_wtf import FlaskForm
import re
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Email, Length, EqualTo, ValidationError


def name_character_check(form, field):
    excluded_chars = "*?!'^+%&/()=}][{$#@<>"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed.")


def character_check(form, field):
    excluded_chars = "*?"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed.")


class RegisterForm(FlaskForm):
    email = StringField(validators=[Required(), Email()])
    firstname = StringField(validators=[Required(), name_character_check])
    lastname = StringField(validators=[Required(), name_character_check])
    phone = StringField(validators=[Required()])
    password = PasswordField(validators=[Required(), Length(min=6, max=12, message="Password must be between 6 and 12 characters in length."), character_check])
    confirm_password = PasswordField(validators=[Required(), EqualTo("password", message="Both passwords fields must be equal.")])
    pin_key = StringField(validators=[Required(), character_check, Length(max=32, min=32, message="Length of PIN key must be 32.")])
    submit = SubmitField(validators=[Required()])

    def validate_password(self, password):
        p = re.compile(r'(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*\W)')
        if not p.match(self.password.data):
            raise ValidationError("Password must contain at least 1 digit, 1 uppercase letter, 1 lower case letter, and no special characters.")

    def validate_phone(self, phone):
        p = re.compile(r'....-...-....')
        if not p.match(self.phone.data):
            raise ValidationError("Phone number must be in format of XXXX-XXX-XXXX, including the dashes")
