from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth


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
            snippet = form.save(commit = False) #если commit = False изменения не сохраняются в базу
            if request.user.is_authenticated:
                snippet.user = request.user #заполянем поле user
                snippet.save() #сохраняем в базу
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
    try:
        snippet = Snippet.objects.get(id = id)
        context = {
            'pagename': 'Просмотр сниппета',
            'snippet': snippet,
            'type': 'view'
            }
        return render (request, 'pages/snippet_detail.html', context)
    except ObjectDoesNotExist:
        Http404

def snippet_delete(request, id): #удаление
    try:
        snippet = Snippet.objects.get(id = id)
        snippet.delete()
        #перенаправление на ту же страницу с которой пришел запрос
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    except ObjectDoesNotExist:
        raise Http404

def snippet_delete(request, id): #редактирование
    try:
        snippet = Snippet.objects.get(id = id)
        snippet.delete()
        #перенаправление на ту же страницу с которой пришел запрос
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except ObjectDoesNotExist:
        raise Http404
    
def snippet_edit(request, id):
    try:
        snippet = Snippet.objects.get(id = id)
    except ObjectDoesNotExist:
        raise Http404
    if request.method == "GET":
        context = {
            'pagename': 'Просмотр сниппета',
            'snippet': snippet,
            'type': 'edit'
            }
        return render (request, 'pages/snippet_detail.html', context)
    if request.method == "POST":
        form_data = request.POST
        snippet.name = form_data["name"]
        snippet.code = form_data["code"]
        snippet.creation_date = form_data["creation_date"]
        snippet.save()
        return redirect('snippets-list')
    
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
        else:
            pass
    return redirect('home')

def logout(request):
    auth.logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))
