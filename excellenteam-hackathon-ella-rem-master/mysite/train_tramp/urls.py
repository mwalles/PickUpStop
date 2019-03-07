# from django.urls import path
#
# from . import views
# app_name = "polls"
#
# urlpatterns = [
#     path('', views.person_list, name='person_list'),
#     # path('person/<int:pk>/', person_detail, name="detail"),
#     path('add/', person_create, name="create"),
#     # path('<int:pk>/', person_detail, name="detail"),
from django.contrib import admin
from django.urls import path, include
from django.urls import path

from .views import Person, person_detail, person_welcome, add_person, screen_app, get_message,run, add_consume

urlpatterns = [
    path('', run, name="run"),
    path('<int:pk>/', screen_app, name="main screen "),
    path('details/', person_welcome, name="details"),
    # path('add_consume/', add_consume, name="add_consume"),
    # path('get_message/', get_message, name="get_message"),
    path('add/', add_person, name="add"),
    path('id/<int:pk>/', person_detail, name="detail"),
    path('add_consume/<int:pk>/', add_consume, name="add_consume"),

]
