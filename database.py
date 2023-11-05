import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def main(userUrl):
    if len(firebase_admin._apps) == 0:
        cred = credentials.Certificate(
            'ub-hackathon-2023-firebase-adminsdk-7l4y4-d2367ecf0b.json')
        firebase_admin.initialize_app(cred, options={
            'databaseURL': 'https://ub-hackathon-2023-default-rtdb.firebaseio.com'
        })

    elif len(firebase_admin._apps) > 0 and ("DBPY" not in firebase_admin._apps.keys()):
        cred = credentials.Certificate(
            'ub-hackathon-2023-firebase-adminsdk-7l4y4-d2367ecf0b.json')
        firebase_admin.initialize_app(cred, name="DBPY", options={
            'databaseURL': 'https://ub-hackathon-2023-default-rtdb.firebaseio.com'
        })
    db_ref = db.reference("/")

    db_ref.child("url").set(str(userUrl))
    db_ref.child("comment").set("")
