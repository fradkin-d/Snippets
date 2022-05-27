"""Snippets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from MainApp import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('registration', views.register, name='registration'),
    path('snippets/list', views.snippets_list, name='list-snippets'),
    path('snippets/my', views.my_snippets_list, name='my-snippets'),
    path('snippet/add', views.add_snippet_page, name='add-snippet'),
    path('snippet/<int:id>', views.snippet_page, name='page-snippet'),
    path('snippet/find', views.snippet_find, name='find-snippet'),
    path('snippet/<int:id>/edit', views.edit_snippet_page, name='edit-snippet'),
    path('snippet/<int:id>/delete', views.delete_snippet, name='delete-snippet'),
    path('comment/add', views.comment_add, name='comment-add'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

