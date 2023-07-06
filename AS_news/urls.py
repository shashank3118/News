from . import views
from django.urls import path

app_name="AS_news"

urlpatterns = [
    path("", views.homepage, name="index"),
    path('politics' , views.PoliticsView , name='politics'),
    path('education' , views.single_news , name='education'),
    path('city' , views.single2_news , name='city'),
    path('features' , views.single3_news , name='features'),
    path('contact.html' , views.contact, name='contact'),
]
