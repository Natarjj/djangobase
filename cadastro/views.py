from django.shortcuts import render

def index(request):
    contexto = {
        'nome': 'Joca',
        'idade': 30,
        'frutas':['Maçã', 'Banana', 'Laranja', 'Uva'],
        }
    return render(request, 'cadastro/index.html', contexto)

def contato(request):
    contexto= {
        "nome" : "joquinha"
    }
    return render(
        request,
          'cadastro/contato.html', 
          contexto)