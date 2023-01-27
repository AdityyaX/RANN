"""rann URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('test/', include('home.urls')),
    path('cricket/', include('home.urls')),
    path('football/', include('home.urls')),
    path('table_tennis/', include('home.urls')),
    path('lawn_tennis/', include('home.urls')),
    path('volleyball/', include('home.urls')),
    path('basketball/', include('home.urls')),
    path('badminton/', include('home.urls')),
    path('pool/', include('home.urls')),
    path('carrom/', include('home.urls')),
    path('chess/', include('home.urls')),
    path('shot_put/', include('home.urls')),
    path('athletics/', include('home.urls')),
    path('kabbadi/', include('home.urls')),
    path('karate/', include('home.urls')),
    path('yoga/', include('home.urls')),
    path('online_games/', include('home.urls')),
]
