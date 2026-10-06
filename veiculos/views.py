from django.shortcuts import render, redirect, get_object_or_404
from .models import Veiculo


def lista_veiculos(request):
    # Verifica se o formulário foi enviado
    if request.method == 'POST':

        # Pega os dados enviados pelo formulário
        placa = request.POST.get('placa')
        ano = request.POST.get('ano')
        cor = request.POST.get('cor')
        categoria = request.POST.get('categoria')

        # Salva o veículo no banco de dados
        Veiculo.objects.create(
            placa=placa,
            ano=ano,
            cor=cor,
            categoria=categoria
        )

        # Volta para a página de veículos
        return redirect('lista_veiculos')

        # Busca todos os veículos cadastrados
    veiculos = Veiculo.objects.all()

    # Envia os veículos para o HTML
    return render(
        request,
        'veiculos/veiculos.html',
        {'veiculos': veiculos}
    )

def excluir_veiculo(request, id):

    veiculo = get_object_or_404(Veiculo,id=id)#Busca o veículo pelo id

    veiculo.delete()

    return redirect('lista_veiculos')

def editar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo,id=id)

    if request.method == 'POST':  # verifica se o formulário foi enviado

        # Pega os dados enviados pelo usuário
        veiculo.placa = request.POST.get('placa')
        veiculo.ano = request.POST.get('ano')
        veiculo.cor = request.POST.get('cor')
        veiculo.categoria = request.POST.get('categoria')


        veiculo.save()  # Salva as alterações no banco de dados

        return redirect('lista_veiculos')  # volta para página de motoristas

    # Abre o formulário preenchido com os dados atuais
    return render(request, 'veiculos/editar_veiculo.html', {'veiculo': veiculo})


