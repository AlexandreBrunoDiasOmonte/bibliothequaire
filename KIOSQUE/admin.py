from django.contrib import admin
from .models import Auteur, Livre, Utilisateur, Editeur, Reservation, Genre


@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_filter = ['genre', 'auteur', 'editeur']
    search_fields = ['titre', 'genre', 'auteur', 'editeur']
    list_display = ['titre', 'auteur', 'genre', 'publication']
    list_per_page = 10
    ordering = ['titre']


@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'email']
    list_per_page = 10
    ordering = ['name']


@admin.register(Auteur)
class AuteurAdmin(admin.ModelAdmin):
    search_fields = ['name', 'userName']
    list_display = ['name', 'userName']
    list_per_page = 10
    if Auteur.name and Auteur.userName:
        ordering = ['name']
    elif Auteur.name and not Auteur.userName:
        ordering = ['name']
    else:
        ordering = ['userName']


@admin.register(Editeur)
class EditeurAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'website', 'phone', 'email']
    list_per_page = 10
    ordering = ['name']


# @admin.register(Reservation)
# class ReservationAdmin(admin.ModelAdmin):
#     search_fields = ['utilisateur', 'reserved']
#     list_display = ['utilisateur', 'reserved', 'created_at']
#     list_per_page = 10
#     ordering = ['-created_at']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ['genre']
    list_display = ['genre']
    ordering = ['genre']
    list_per_page = 10
