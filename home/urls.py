#  This file is made manually

from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name = 'Home' ),
    
    path('home', views.index, name = 'Home' ),

    path("about", views.about, name = 'About' ),
    
    path("contact", views.contact, name = 'Contact' ),

    path("python", views.pyton, name = 'Pyton' ),

    path("django", views.jango, name = 'jango' ),

    path("front", views.front, name = 'front' ),

    path("java", views.javas, name = 'javas' ),

    path("css", views.csss, name = 'csss' ),

    path("cpp", views.cpplus, name = 'cpplus' ),

    path("registration", views.registration, name = 'registration' ),

]