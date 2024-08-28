from django.urls import path
from . import views
# from . = from this directory

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
]
