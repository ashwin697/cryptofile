from django.contrib import admin
from django.urls import path
from . import views
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings

urlpatterns = [

    path('',views.home,name='home'),
    path("cf/contact/", views.contact, name="contact"),
    path("cf/encrypt/", views.encrypt, name="encrypt"),
    path("cf/decrypt/", views.decrypt, name="decrypt"),
    path("cf/about/", views.about, name="about"),
    path("cf/encrypted/", views.encrypted, name="encrypted"),
    path("cf/decrypted/", views.decrypted, name="decrypted"),
    path("cf/wordenc/", views.wordenc, name="wordenc"),
    path("cf/worddec/", views.worddec, name="worddec"),
]