from django.urls import path

from src.views import ShowContactPage, ShowMainPage


app_name = 'src'

urlpatterns = [
    path('', ShowMainPage.as_view(), name='main'),
    path('contacts/', ShowContactPage.as_view(), name='contacts'),
]
