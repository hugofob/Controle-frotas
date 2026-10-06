from django.shortcuts import render, redirect,  get_object_or_404
from .models import comentario

def comentarios(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        texto = request.POST.get('comentario')
        receber_info = request.POST.get('receber_info') == 'on'

        comentario.objects.create(
            nome=nome,
            email=email,
            comentario=texto,
            receber_info=receber_info
        )

        return redirect('comentarios')

    comentarios_lista = comentario.objects.all()

    return render(
        request,
        'comentarios/comentarios.html',
        {'comentarios': comentarios_lista}
    )

def excluir_comentario(request, id):
    comentario_obj = get_object_or_404(comentario, id=id)
    comentario_obj.delete()
    return redirect('comentarios')


def editar_comentario(request, id):

    comentario_obj = get_object_or_404(comentario, id=id)

    if request.method == 'POST':
        comentario_obj.nome = request.POST.get('nome')
        comentario_obj.email = request.POST.get('email')
        comentario_obj.comentario = request.POST.get('comentario')
        comentario_obj.receber_info = request.POST.get('receber_info') == 'on'

        comentario_obj.save()

        return redirect('comentarios')

    return render(
        request,
        'comentarios/editar_comentario.html',
        {'comentario': comentario_obj}
    )
