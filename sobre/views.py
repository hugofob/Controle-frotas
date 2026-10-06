from django.shortcuts import render

def sobre(request):
    return render(request, 'sobre/sobre.html')

def manutencao(request):
    return render(request, 'sobre/manutencao.html')

def oficinas(request):
    return render(request, 'sobre/oficinas.html')

def postos(request):
    return render(request, 'sobre/postos.html')

def borracharia(request):
    return render(request, 'sobre/borracharia.html')