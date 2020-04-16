from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime
from .models import Article


# Create your views here.
def home(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all()  # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})


def lire(request, id, slug=1):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article':article})


def list_articles(request, year, month=1):
    """ Liste des articles d'un mois précis. """
    return HttpResponse(
        "Vous avez demandé les articles de {0} {1}.".format(month, year)
    )


def list_articles_by_tag(request, tag):
    return HttpResponse(
        "Vous avez demandé les articles avec le tag {0}.".format(tag)
    )


def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nb1, nb2):
    total = nb1 + nb2
    # Retourne nb1, nb2 et total
    return render(request, 'blog/addition.html', locals())


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


def testbase(request):
    return render(request, 'blog/TestBase.html')
