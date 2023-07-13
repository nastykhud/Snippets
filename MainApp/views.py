from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == 'GET': #Чтобы отобразить чистую форму
        form = SnippetForm()
        context = {
        'pagename': 'Добавление нового сниппета',
        'form': form
        }
        return render(request, 'pages/add_snippet.html', context)
    if request.method == 'POST': #Чтобы взять данные в базу по нажатию кнопки Submitt
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snippets-list')
        return render(request, 'pages/add_snippet.html', {'form': form}) #на случай неверного заполнения формы
 

def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        'pagename': 'Просмотр сниппетов',
         'snippets': snippets 
         }
    return render(request, 'pages/view_snippets.html', context)

def snippet_detail(request, id):
    snippet = Snippet.objects.get(id = id)
    context = {
        'pagename': 'Просмотр сниппета',
        'snippet': snippet
        }
    return render (request, 'pages/snippet_detail.html', context)

def snippet_delete(request, id): #удаление
    snippet = Snippet.objects.get(id = id)
    snippet.delete()
    #перенаправление на ту же страницу с которой пришел запрос
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

