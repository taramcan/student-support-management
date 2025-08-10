import flask
from flask import Blueprint, render_template, request, jsonify
from app.models.student import Student
from firebase_admin import firestore
from app.db import db

bp = Blueprint('main', __name__)



#starting page
@bp.route('/', methods = ['GET'])
def index():
    return(render_template('index.html'))

@bp.route('/main_menu', methods = ['GET'])
def main_menu():
    return(render_template('main_menu.html'))

@bp.route('/annual_renewal')
def annual_renewal():
    teachers_ref = db.collection('teachers')
    docs = teachers_ref.stream()

    teachers = []
    for doc in docs:
        t = doc.to_dict()
        t['full_name'] = f"{t['last_name']}, {t['first_name']}"
        teachers.append(t)
    
    return render_template('annual_renewal.html', teachers = teachers)

@bp.route("/save_student", methods = ["POST"])
def save_student():
    data = request.get_json()
    student_laid = data.get('laid', '').strip()

    student_ref = db.collection('students').document(student_laid)
    student_doc = student_ref.get()

    if student_doc.exists:
        student_ref.update(data)
    else:
        student_ref.set(data)

    return render_template('main_menu.html')


