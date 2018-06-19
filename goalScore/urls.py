"""goalScore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from goalScoreApp import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('matches/', views.matches),
                  path('match/', views.match),
                  path('teams/', views.teams),
                  path('team/', views.team),
                  path('players/', views.players),
                  path('player/', views.player),
                  path('standing/', views.groupStanding),
                  path('upcoming_matches/', views.upcoming_match),
                  path('todays_matches/', views.todays_match),
                  path('recent_matches/', views.recent_match),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
