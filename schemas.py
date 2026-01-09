from marshmallow import Schema, fields, validates, ValidationError
import re
class RegisterSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    passwordConfirm = fields.String(required=True)
    role = fields.String()
    @validates('password')
    def validate_password(self, value):
        if len(value) < 8 or not re.search(r'\d', value) or not re.search(r'[A-Z]', value):
            raise ValidationError('Password must be at least 8 chars, contain a digit and an uppercase letter')
class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
class UpdateSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String()
    role = fields.String()
