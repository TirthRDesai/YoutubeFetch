import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(
    'ub-hackathon-2023-firebase-adminsdk-7l4y4-d2367ecf0b.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ub-hackathon-2023.firebaseio.com/'
})


def main(userUrl):

    ref = db.reference()
    ref.set({
        'data': {
            'url': userUrl
        }
    })
