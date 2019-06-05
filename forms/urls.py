"""tutorials URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.FormListView.as_view(), name='post_list'),
    path('list/', views.FormListView.as_view(), name='post_list'),
    path('<int:pk>', views.FormDetailView.as_view(), name='post_view'),
    path('add/', views.FormCreateView.as_view(), name='post_add'),
    path('<int:pk>/edit/', views.FormUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.FormDeleteView.as_view(), name='post_delete'),
]
