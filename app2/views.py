from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Soy el index de la App2</h1>")

def text(request):
    return HttpResponse("""<h2 style="color:blue"> Titulo de ejemplo</h2>
                        <p>Soy un texto de ejemplo de la App2</p>
                        <a href="/app2">Volver</a>
                        """)