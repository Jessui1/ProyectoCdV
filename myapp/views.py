from django.shortcuts import render

# Create your views here.
def index(request):
    contexto = {"mensaje": "Bienvenidos a mi aplicacion Django"}
    return render(request, 'myapp/index.html', contexto)