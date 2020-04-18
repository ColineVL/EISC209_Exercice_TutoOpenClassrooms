from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime
from .models import Article


# Create your views here.
def accueil(request):
    return render(request, 'blog/accueil.html')


def bienvenue(request, sexe, age, prenom):
    couleurs = {
        'FF0000': 'rouge',
        'ED7F10': 'orange',
        'FFFF00': 'jaune',
        '00FF00': 'vert',
        '0000FF': 'bleu',
        '4B0082': 'indigo',
        '660099': 'violet',
    }
    return render(request, 'blog/bienvenue.html', locals())


def lecture(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire_article.html', {'article': article})


def articles(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all()  # Nous sélectionnons tous nos articles
    return render(request, 'blog/tous_articles.html', {'derniers_articles': articles})


def contributeurs(request):
    return render(request, 'blog/contributeurs.html')