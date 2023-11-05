import firebase_admin
from firebase_admin import credentials


def main(userUrl):
    if len(firebase_admin._apps) == 0:
        cred = credentials.Certificate(
            'ub-hackathon-2023-firebase-adminsdk-7l4y4-d2367ecf0b.json')
        firebase_admin.initialize_app(cred, options={
            'databaseURL': 'https://ub-hackathon-2023.firebaseio.com/'
        })
    else:
        if "DATABASEPY" not in firebase_admin._apps.keys():
            cred = credentials.Certificate(
                'ub-hackathon-2023-firebase-adminsdk-7l4y4-d2367ecf0b.json')
            firebase_admin.initialize_app(cred, name="DATABASEPY", options={
                'databaseURL': 'https://ub-hackathon-2023.firebaseio.com/'
            })

    firebase_admin.db = firebase_admin.db.reference("/")
    print(firebase_admin._apps)
    print(db.get())
    db.set({
        "data": {
            'url': str(userUrl),
            'comments': ""
        }})
