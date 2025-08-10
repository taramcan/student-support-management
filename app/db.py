import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("app/config/student-support-tracker-firebase-adminsdk-fbsvc-e321329916.json")

firebase_admin.initialize_app(cred)

db = firestore.client()
