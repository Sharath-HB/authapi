import firebase_admin
from firebase_admin import credentials, db

# Replace with the path to your service account JSON file
cred = credentials.Certificate(r"C:\Users\dhanu\Downloads\auth-f4e76-firebase-adminsdk-jlghr-cd68c54e38.json")

firebase = firebase_admin.initialize_app(cred, {
    "databaseURL": "https://auth-f4e76.firebaseio.com"
})
