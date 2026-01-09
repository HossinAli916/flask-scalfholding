from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from models import db, User
from schemas import UpdateSchema
from passlib.hash import bcrypt
users_bp = Blueprint('users', __name__)
@users_bp.route('/', methods=['GET'])
@jwt_required()
def list_users():
    users = User.query.with_entities(User.id, User.name, User.email, User.role).all()
    result = [{'id': u.id, 'name': u.name, 'email': u.email, 'role': u.role} for u in users]
    return jsonify(result)
@users_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    claims = get_jwt()
    current_id = get_jwt_identity()
    data = request.get_json() or {}
    errors = UpdateSchema().validate(data)
    if errors:
        return jsonify({'errors': errors}), 400
    if claims.get('role') != 'Admin' and current_id != user_id:
        return jsonify({'message': 'Forbidden'}), 403
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user.name = data['name']
    user.email = data['email']
    if data.get('password'):
        user.password_hash = bcrypt.hash(data['password'])
    if data.get('role') and claims.get('role') == 'Admin':
        user.role = data['role']
    db.session.commit()
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email, 'role': user.role})
@users_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    claims = get_jwt()
    current_id = get_jwt_identity()
    if claims.get('role') != 'Admin' and current_id != user_id:
        return jsonify({'message': 'Forbidden'}), 403
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Deleted'})
