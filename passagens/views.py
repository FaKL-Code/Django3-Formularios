from django.shortcuts import render
from passagens.forms import PassagensForms

# Create your views here.
def index(request):
    form = PassagensForms()
    contexto = {'form': form}
    return render(request, 'index.html', contexto)

def minha_consulta(request):
    if request.method == "POST":
        form = PassagensForms(request.POST)
        contexto = {'form': form}
    return render(request, 'minha_consulta.html', contexto)