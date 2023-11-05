import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def main(userUrl):
    try:
        if not firebase_admin._apps:
            cred = credentials.Certificate(
                'ub-hackathon-2023-firebase-adminsdk-7l4y4-d2367ecf0b.json')
            firebase_admin.initialize_app(cred, name="FLASK_APP", options={
                'databaseURL': 'https://ub-hackathon-2023.firebaseio.com/'
            })
        ref = db.reference("/")
        ref.set({
            'data': {
                'url': str(userUrl)
            }
        })
    except Exception as e:
        print(e)
