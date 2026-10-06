from django.shortcuts import render, redirect
from .models import Motorista


def motoristas(request):

    # Verifica se o formulário foi enviado
    if request.method == 'POST':

        # Pega os dados enviados pelo formulário
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        cnh = request.POST.get('cnh')
        categoria = request.POST.get('categoria')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')

        # Cria o motorista no banco de dados
        Motorista.objects.create(
            nome=nome,
            endereco=endereco,
            cnh=cnh,
            categoria=categoria,
            telefone=telefone,
            email=email
        )

        # Volta para a página de motoristas
        return redirect('motoristas')

    # Busca todos os motoristas cadastrados
    lista_motoristas = Motorista.objects.all()

    # Envia os motoristas para o HTML
    return render(
        request,
        'motoristas/motoristas.html',
        {
            'motoristas': lista_motoristas
        }
    )

def excluir_motorista(request, id):

    motorista = Motorista.objects.get(id=id)

    motorista.delete()

    return redirect('motoristas')

def editar_motorista(request, id):
    motorista = Motorista.objects.get(id=id)#busca o motoristo pelo id

    if request.method == 'POST':#verifica se o formulário foi enviado

        #Pega os dados enviados pelo usuário
        motorista.nome = request.Post.get('nome')
        motorista.endereco = request.POST.get('endereco')
        motorist.cnh = request.POST.get('cnh')
        motorista.categoria = request.POST.get('categoria')
        motorista.telefone = request.POST.get('telefone')
        motorista.email = request.POST.get('email')

        motorista.save()#Salva as alterações no banco de dados

        return redirect('motoristas')#volta para página de motoristas

    #Abre o formulário preenchido com os dados atuais
    return render(request, 'motoristas/editar_motoristas.html',{'motoristas':motorista})




