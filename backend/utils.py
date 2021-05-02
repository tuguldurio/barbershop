import bcrypt
from database import db

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(password_input, password):
	return bcrypt.checkpw(password_input.encode(), password)

def account_exists(email):
    return db.get_collection('accounts').count_documents({'email': email})

def create_user(email, password):
    db.get_collection('accounts').insert_one({'email': email, 'password': password})