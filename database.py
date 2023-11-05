import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def main(userUrl):

    # As an admin, the app has access to read and write all data, regradless of Security Rules
    # Fetch the service account key JSON file contents
    if (not credentials.Certificate(
            'ub-hackathon-2023-firebase-adminsdk-7l4y4-d2367ecf0b.json')):
        cred = credentials.Certificate(
            'ub-hackathon-2023-firebase-adminsdk-7l4y4-d2367ecf0b.json')
    if not firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://ub-hackathon-2023.firebaseio.com/'
    }):
        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://ub-hackathon-2023.firebaseio.com/'
        })
    ref = db.reference("/data")
    ref.delete()
    ref = db.reference('/data/'+str(userUrl))
    ref.set({
        'url': str(userUrl)
    })
