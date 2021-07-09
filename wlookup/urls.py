# This is my urls.py file

from django.urls import path
from . import views #the "." means current directory

urlpatterns = [
	path('',views.home, name="home"),
	path('about.html',views.about, name="about")
]
