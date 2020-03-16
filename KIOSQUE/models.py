from django.db import models


class Auteur(models.Model):
    name = models.CharField('Nom', max_length=25)
    surname = models.CharField('Prénom', max_length=25)
    photo = models.URLField('Photo', blank=True)
    birthDate = models.DateField('Date de naissance', blank=True)
    deathDate = models.DateField('Date de décès', blank=True)


class Editeur(models.Model):
    name = models.CharField('Nom', max_length=200)
    website = models.URLField('Site internet', max_length=200, blank=True)
    phone = models.CharField('Téléphone', max_length=13, blank=True)
    adresse = models.CharField('Adresse', max_length=200, blank=True)
    email = models.EmailField('Email', max_length=50, blank=True)


class Contact(models.Model):
    name = models.CharField('Nom', max_length=200)
    email = models.EmailField('Email', max_length=100)
    photo = models.URLField('Photo', blank=True)


class Book(models.Model):
    titre = models.CharField('Titre du livre', max_length=200)
    available = models.BooleanField('Disponneble ?', default=True)
    parution = models.DateField('Date de parution')
    nbPages = models.PositiveIntegerField('Nombre de pages')
    nature = models.CharField('Nature du livre', max_length=200)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    editeur = models.ManyToManyField(Editeur, related_name="books")
    couverture = models.URLField('Image de courverture', blank=True)
    resume = models.TextField('Résumé')


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    reserved = models.BooleanField('Réservé ?', default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
