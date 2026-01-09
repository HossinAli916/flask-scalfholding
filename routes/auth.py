from flask import Blueprint, request, jsonify
from models import db, User
from schemas import RegisterSchema, LoginSchema
from passlib.hash import bcrypt
from flask_jwt_extended import create_access_token
auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    errors = RegisterSchema().validate(data)
    if errors:
        return jsonify({'errors': errors}), 400
    if data.get('password') != data.get('passwordConfirm'):
        return jsonify({'message': 'Passwords do not match'}), 400
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already in use'}), 400
    hashed = bcrypt.hash(data['password'])
    user = User(name=data['name'], email=data['email'], password_hash=hashed, role=data.get('role') or 'User')
    db.session.add(user)
    db.session.commit()
    token = create_access_token(identity=user.id, additional_claims={'role': user.role})
    return jsonify({'token': token, 'user': {'id': user.id, 'name': user.name, 'email': user.email, 'role': user.role}}), 201
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    errors = LoginSchema().validate(data)
    if errors:
        return jsonify({'errors': errors}), 400
    user = User.query.filter_by(email=data['email']).first()
    if not user or not bcrypt.verify(data['password'], user.password_hash):
        return jsonify({'message': 'Invalid credentials'}), 400
    token = create_access_token(identity=user.id, additional_claims={'role': user.role})
    return jsonify({'token': token}), 200
