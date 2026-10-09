from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from cadastro.forms import ContatoForm, PessoaForm 
from cadastro.models import Pessoa

def index(request):
# Recebe todas as "Pessoas" do banco de dados
    pessoas = Pessoa.objects.order_by('nome', 'email')

# Conta o total de registrtos
    total = Pessoa.objects.count()
    
    contexto = {
        'nome': 'Joca',
        'pessoas': pessoas,
        'total': total 
        }
    return render(
        request, 
        'cadastro/index.html', 
        contexto)

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contato')
    else:
        form = ContatoForm()
    return render(
        request,
          'cadastro/adicionar.html',
          {'form': form, 'nome' : 'Joca'}
          )
           
@login_required
def adicionar(request):
    # Se o form está sendo enviando
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        # Exibe o formoulário
        form = PessoaForm()
    return render(
        request,
          'cadastro/adicionar.html',
            {'form': form, 'nome' : 'Joca'})

def detalhe(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)

    return render(request, 'cadastro/detalhe.html',
 { 'pessoa' : pessoa,'nome' : 'Joca'})

def editar(request, id):

    #Obtém os da pessoa pelo ID
    pessoa = get_object_or_404(Pessoa, id=id)

    # Se o formulário foi enviado
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('detalhe', id=id)
    else:
        form = PessoaForm(instance=pessoa)
    return render(
        request, 'cadastro/editar.html',
          {'form': form,
            'pessoa': pessoa,
            'nome' : 'Joca'})

def deletar(request, id):
    #Obtém os da pessoa pelo ID
    pessoa = get_object_or_404(Pessoa, id=id)
    # Se o formulário foi enviado
    if request.method == 'POST':
        pessoa.delete()
        return redirect('index')
    return render(
        request, 'cadastro/deletar.html',
          {'pessoa': pessoa}
)