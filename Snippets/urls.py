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
    path('snippets/add', views.add_snippet_page, name='add-snippet'),
    # path('snippets/edit/<int:id>', views.edit_snippet_page, name='edit-snippet'),
    path('snippets/list', views.snippets_list, name='list-snippets'),
    path('snippet/<int:id>', views.snippet_page, name='page-snippet'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

