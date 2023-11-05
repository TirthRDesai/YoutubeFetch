import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def main(userUrl):
    try:
        cred = credentials.Certificate(
            'ub-hackathon-2023-firebase-adminsdk-7l4y4-d2367ecf0b.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://ub-hackathon-2023.firebaseio.com/'
        }, name="FLASK_APP")
        ref = db.reference("/")
        ref.set({
            'data': {
                'url': str(userUrl)
            }
        })
    except Exception as e:
        print(e)
