from django.urls import path

from src.views import (
    ShowContactPage,
    ShowMainPage,
    ShowUserAgreementPage,
    ShowPrivacyPolicyPage,
)


app_name = "src"

urlpatterns = [
    path("", ShowMainPage.as_view(), name="main"),
    path("contacts/", ShowContactPage.as_view(), name="contacts"),
    path('privacy_policy/', ShowPrivacyPolicyPage.as_view(), name='privacy_policy'),
    path('user_agreement/', ShowUserAgreementPage.as_view(), name='user_agreement'),
]
