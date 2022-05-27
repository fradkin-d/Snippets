from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from MainApp.models import Snippet, LANGS
from MainApp.forms import SnippetForm, UserRegistrationForm, CommentForm
from django.core.exceptions import ObjectDoesNotExist


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


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


def snippets_list(request):
    context = {
        'pagename': 'Публичные сниппеты',
        'snippets': Snippet.objects.filter(is_public=True),
        'USER_TZ': 'Europe/Moscow',
        'langs': [('all', 'Все')] + LANGS,
        'lang_filter': 'all',
    }
    if request.method == 'POST':
        print(request.POST)
        context.update({
            'lang_filter': request.POST.get('lang_filter')
        })
    return render(request, 'pages/view_snippets.html', context)


@login_required
def my_snippets_list(request):
    context = {
        'pagename': 'Мои сниппеты',
        'snippets': Snippet.objects.filter(user=request.user),
        'USER_TZ': 'Europe/Moscow',
        'langs': [('all', 'Все')] + LANGS,
        'lang_filter': 'all',
    }
    if request.method == 'POST':
        print(request.POST)
        context.update({
            'lang_filter': request.POST.get('lang_filter')
        })
    return render(request, 'pages/view_snippets.html', context)


def add_snippet_page(request):
    if request.method == 'GET':
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form,
        }
        return render(request, 'pages/edit_snippet.html', context)
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            return redirect("my-snippets")


def snippet_page(request, id=None):
    snippet = Snippet.objects.get(pk=id)
    comment_form = CommentForm()
    context = {
        'pagename': 'Страница сниппета',
        'snippet': snippet,
        'comment_form': comment_form,
        'comments': snippet.comments.all(),
        'USER_TZ': 'Europe/Moscow',
    }
    return render(request, 'pages/page_snippet.html', context)


def snippet_find(request):
    id = request.POST.get('snippet_id')
    try:
        snippet = Snippet.objects.get(pk=id)
        return redirect('page-snippet', id)
    except ObjectDoesNotExist:
        return redirect('home')


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


@login_required
def delete_snippet(request, id):
    snippet = Snippet.objects.get(pk=id)
    if snippet.user == request.user:
        snippet.delete()
    return redirect("my-snippets")


def comment_add(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.snippet = Snippet.objects.get(pk=request.POST.get('snippet_id'))
            comment.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return Http404
