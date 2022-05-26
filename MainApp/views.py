from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm, UserRegistrationForm
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
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            return redirect("my-snippets")


def edit_snippet_page(request, id):
    snippet = Snippet.objects.get(pk=id)
    if request.method == 'GET':
        form = SnippetForm(instance=snippet)
        context = {
            'pagename': 'Редактирование сниппета',
            'form': form,
        }
        return render(request, 'pages/edit_snippet.html', context)
    if request.method == 'POST':

        snippet.name = request.POST.get('name')
        snippet.lang = request.POST.get('lang')
        snippet.code = request.POST.get('code')
        snippet.is_public = request.POST.get('is_public') == 'on'
        snippet.save()
        return redirect("my-snippets")


def snippets_list(request):
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': Snippet.objects.filter(is_public=True),
        'USER_TZ': 'Europe/Moscow',
        'edit': False,
        'delete': False,
    }
    return render(request, 'pages/view_snippets.html', context)


@login_required
def my_snippets_list(request):
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': Snippet.objects.filter(user=request.user),
        'USER_TZ': 'Europe/Moscow',
        'edit': True,
        'delete': True,
    }
    return render(request, 'pages/view_snippets.html', context)


def snippet_page(request, id):
    context = {
        'pagename': 'Страница сниппета',
        'snippet': Snippet.objects.get(pk=id),
        'USER_TZ': 'Europe/Moscow',
    }
    return render(request, 'pages/page_snippet.html', context)


def login(request):
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


def logout(request):
    auth.logout(request)
    return redirect('home')


def register(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        context = {'pagename': 'Регистрация пользователя', 'form': form}
        return render(request, 'pages/registration.html', context)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        context = {'pagename': 'Регистрация пользователя', 'form': form}
        return render(request, 'pages/registration.html', context)
