
from django.urls import path
from .views import home, create_website

urlpatterns = [
    path('', home, name="home"),
    path('create-website/', create_website, name="create_website"),
]