from django.urls import path
from main_app import views

app_name = 'main_app'

urlpatterns = [
    path("", views.index, name='index')
]
