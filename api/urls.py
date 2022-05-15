from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('api/', views.quiz_view, name='quiz-view')
]

