import pyrebase
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import auth as firebase_auth

from django.conf import settings

firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
auth = firebase.auth()

class SendOTPView(APIView):
    def post(self, request):
        phone_number = request.data.get("phone_number")
        if not phone_number:
            return Response({"error": "Phone number is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Send OTP (Firebase automatically sends OTP)
            firebase_auth.create_user(phone_number=phone_number)
            return Response({"message": f"OTP sent to {phone_number}."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class VerifyOTPAndRegisterView(APIView):
    def post(self, request):
        id_token = request.data.get("id_token")  # Firebase ID token received after OTP verification in client-side
        if not id_token:
            return Response({"error": "ID token is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            decoded_token = firebase_auth.verify_id_token(id_token)
            uid = decoded_token["uid"]
            phone_number = decoded_token.get("phone_number")

            # Save user to Firebase database (optional)
            db = firebase.database()
            db.child("users").child(uid).set({
                "phone_number": phone_number,
                "uid": uid,
            })
            return Response({"message": "User registered successfully.", "uid": uid}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
