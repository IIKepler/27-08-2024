from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    html="""
    <h1> Soy el index de la App1</h1>
    <h2> Hola!</h2>
    """
    return HttpResponse(html)

def text(request):
    html="""<h1 style="color:red"> Este es un ejemplo</h1>
    <p> Este es un ejemplo de texto que es para ver como funcionan las diferentes funciones</p>
    """
    return HttpResponse(html)