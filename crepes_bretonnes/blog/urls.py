"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.accueil),
    path('accueil', views.accueil, name="accueil"),
    path('bienvenue/<str:sexe>/<int:age>/<str:prenom>/', views.bienvenue, name='bienvenue'),
    path('tousArticles', views.articles, name="tousArticles"),
    path('article/<int:id>-<slug:slug>', views.lecture, name="lire_article"),
    path('contributeurs', views.contributeurs, name="contributeurs"),
    path('contactUs/', views.contact_us, name='contact_us'),
    path('accueil/proposerArticle', views.proposer_article, name='proposer_article'),
    path('contributeurs/inscription', views.inscription, name="inscription"),
    path('accueil/newUser', views.new_user, name="new_user"),

    url(r'^connexion$', views.connexion, name='connexion'),
    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),

    #path(r'^connexion$', auth_views.login, {'template_name': 'auth/connexion.html'}),
]
