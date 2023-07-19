from django.urls import path

from .views import home

urlpatterns = [
    path('lesson_4/', home)

]