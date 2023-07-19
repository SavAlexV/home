from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("""
    
    <h1 style= "background-color: orange; text-align: center; border: solid; border-radius: 10px;">Домашка по 4 занятию</h1>
    
    """)


