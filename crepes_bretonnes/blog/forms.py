from django import forms
from django.contrib.auth.models import User

from .models import Article, Profil


class ContactUsForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

    def clean_message(self):
        message = self.cleaned_data['message']
        if "gaufres" in message:
            raise forms.ValidationError("On ne veut pas entendre parler de gaufres !")

        return message  # Ne pas oublier de renvoyer le contenu du champ traité

    def clean(self):
        cleaned_data = super(ContactUsForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        if sujet and message:  # Est-ce que sujet et message sont valides ?
            if "pizza" in sujet and "pizza" in message:
                self.add_error("message",
                               "Vous parlez déjà de pizzas dans le sujet, "
                               "n'en parlez plus dans le message !"
                               )

        return cleaned_data  # N'oublions pas de renvoyer les données si tout est OK


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class ContributeurForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()


class NewUserForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(label="Votre adresse e-mail")
    password = forms.CharField()
    site_web = forms.URLField()
    avatar = forms.ImageField()
    signature = forms.CharField()
    inscrit_newsletter = forms.BooleanField()


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)