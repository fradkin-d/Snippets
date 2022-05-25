from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
from django.contrib import auth


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == 'GET':
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form,
        }
        return render(request, 'pages/add_snippet.html', context)
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list-snippets")


def snippets_list(request):
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': Snippet.objects.all(),
        'USER_TZ': 'Europe/Moscow',
    }
    return render(request, 'pages/view_snippets.html', context)


def snippet_page(request, id):
    context = {
        'pagename': 'Страница сниппета',
        'snippet': Snippet.objects.get(pk=id),
        'USER_TZ': 'Europe/Moscow',
    }
    return render(request, 'pages/page_snippet.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            pass
    return redirect('home')
