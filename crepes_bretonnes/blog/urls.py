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

from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home, name="accueil"),
    path('article/<int:id_article>$', views.view_article, name='afficher_article'),
    path('articles/<str:tag>', views.list_articles_by_tag),
    path('articles/<int:year>/<int:month>', views.list_articles),
    path('redirection', views.view_redirection),
    path('date', views.date_actuelle),
    path('addition/<int:nb1>/<int:nb2>/', views.addition),
    path('bienvenue/<str:sexe>/<int:age>/<str:prenom>/', views.bienvenue, name='bienvenue'),
    path('testBase', views.testbase),
]
