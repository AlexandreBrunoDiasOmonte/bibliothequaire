from django.db import models


class Auteur(models.Model):
    name = models.CharField("Nom de l'auteur", max_length=50)
    userName = models.CharField("Nom d'usage", max_length=50, blank=True)
    photo = models.URLField('Photo', blank=True)

    def __str__(self):
        if self.userName == "":
            return self.name
        else:
            return self.userName


class Editeur(models.Model):
    name = models.CharField("Nom de l'éditeur", max_length=200)
    website = models.URLField('Site internet', max_length=200, blank=True)
    phone = models.CharField('Téléphone', max_length=18, blank=True)
    adresse = models.CharField('Adresse', max_length=200, blank=True)
    email = models.EmailField('Email', max_length=50, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    genre = models.CharField('Genre du livre', max_length=100, blank=True)

    def __str__(self):
        return self.genre


class Utilisateur(models.Model):
    name = models.CharField('Nom', max_length=200)
    email = models.EmailField('Email', max_length=100)
    photo = models.URLField('Photo', blank=True)
    adresse = models.CharField('Adresse', max_length=200, blank=True)
    phone = models.CharField('Téléphone', max_length=18, blank=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    reserved = models.BooleanField('Réservé ?', default=False)
    utilisateur_id = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)


class Livre(models.Model):
    titre = models.CharField('Titre du livre', max_length=200)
    available = models.BooleanField('Disponneble ?', default=True)
    parution = models.DateField('Date de parution')
    nbPages = models.PositiveIntegerField('Nombre de pages', blank=True, null=True)
    couverture = models.URLField('Image de courverture', blank=True)
    resume = models.TextField('Résumé', blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    editeur = models.ManyToManyField(Editeur, related_name="livres")
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    Reservation_id = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
