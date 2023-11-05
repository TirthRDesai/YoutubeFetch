import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
if len(firebase_admin._apps) == 0:
    cred = credentials.Certificate(
        'ub-hackathon-2023-firebase-adminsdk-7l4y4-d2367ecf0b.json')
    firebase_admin.initialize_app(cred, options={
        'databaseURL': 'https://ub-hackathon-2023.firebaseio.com/'
    })
else:
    cred = credentials.Certificate(
        'ub-hackathon-2023-firebase-adminsdk-7l4y4-d2367ecf0b.json')
    firebase_admin.initialize_app(cred, name="DATABASEPY", options={
        'databaseURL': 'https://ub-hackathon-2023.firebaseio.com/'
    })


def main(userUrl):
    try:
        print(firebase_admin._apps)
        db = db.reference("/")
        print(db.get())
        db.set({
            "data": {
                'url': str(userUrl),
                'comments': ""
            }})
    except Exception as e:
        print(e)
