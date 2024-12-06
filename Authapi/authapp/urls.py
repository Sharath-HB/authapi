from django.urls import path
from .views import SendOTPView, VerifyOTPAndRegisterView

urlpatterns = [
    path("send-otp/", SendOTPView.as_view(), name="send_otp"),
    path("verify-register/", VerifyOTPAndRegisterView.as_view(), name="verify_register"),
]
