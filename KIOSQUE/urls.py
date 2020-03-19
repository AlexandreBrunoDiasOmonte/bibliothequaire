from django.urls import path, include

from . import views

app_name = "KIOSQUE"
urlpatterns = [
    path('', views.kiosque, name="kiosque"),
    path('details/<int:livre_id>', views.details, name="détails"),
    path('search/', views.recherche, name="recherche")
]
