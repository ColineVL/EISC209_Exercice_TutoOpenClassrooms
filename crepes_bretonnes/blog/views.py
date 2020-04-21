from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime

from django.urls import reverse

from .models import Article, Contributeur, Profil
from .forms import ArticleForm, ContributeurForm, ContactUsForm, NewUserForm, ConnexionForm


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
    return render(request, 'blog/lireArticle.html', {'article': article})


def articles(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all()  # Nous sélectionnons tous nos articles
    return render(request, 'blog/tousArticles.html', {'derniers_articles': articles})


def contributeurs(request):
    return render(request, 'blog/contributeurs.html', {'contributeurs': Contributeur.objects.all()})


def contact_us(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactUsForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/contactUs.html', locals())


@login_required(login_url='blog/connexion')
def proposer_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        envoi = True
    return render(request, 'blog/proposerArticle.html', locals())


def inscription(request):
    sauvegarde = False
    form = ContributeurForm(request.POST or None, request.FILES)
    if form.is_valid():
        contributeur = Contributeur()
        contributeur.nom = form.cleaned_data["nom"]
        contributeur.adresse = form.cleaned_data["adresse"]
        contributeur.photo = form.cleaned_data["photo"]
        contributeur.save()
        sauvegarde = True
        return redirect('contributeurs')

    return render(request, 'blog/contributeurInscription.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })


def new_user(request):
    sauvegarde = False
    form = NewUserForm(request.POST or None, request.FILES)
    if form.is_valid():
        user = User()
        user.username = form.cleaned_data["username"]
        user.email = form.cleaned_data["email"]
        user.password = form.cleaned_data["password"]
        user.save()
        profil = Profil()
        profil.user = user
        profil.site_web = form.cleaned_data["site_web"]
        profil.avatar = form.cleaned_data["avatar"]
        profil.signature = form.cleaned_data["signature"]
        profil.inscrit_newsletter = form.cleaned_data["inscrit_newsletter"]
        profil.save()
        sauvegarde = True
        return redirect('accueil')
    return render(request, 'blog/newUser.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else:  # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'blog/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))
