from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("test/", views.test, name="test"),
    path("cricket/", views.cricket, name="cricket"),
    path("football/", views.football, name="football"),
    path("table_tennis/", views.table_tennis, name="table_tennis"),
    path("lawn_tennis/", views.lawn_tennis, name="lawn_tennis"),
    path("volleyball/", views.volleyball, name="volleyball"),
    path("basketball/", views.basketball, name="basketball"),
    path("badminton/", views.badminton, name="badminton"),
    path("pool/", views.pool, name="pool"),
    path("carrom/", views.carrom, name="carrom"),
    path("chess/", views.chess, name="chess"),
    path("shot_put/", views.shot_put, name="shot_put"),
    path("athletics/", views.athletics, name="athletics"),
    path("kabbadi/", views.kabbadi, name="kabbadi"),
    path("karate/", views.karate, name="karate"),
    path("yoga/", views.yoga, name="yoga"),
    path("online_games/", views.online_games, name="online_games"),
    path("coremember/", views.coremember, name="coremember"),
]
