# Generated by Django 3.0.4 on 2020-03-20 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="Nom de l'auteur")),
                ('userName', models.CharField(blank=True, max_length=50, verbose_name="Nom d'usage")),
                ('photo', models.URLField(blank=True, verbose_name='Photo')),
                ('birthDate', models.DateField(blank=True, verbose_name='Date de naissance')),
                ('deathDate', models.DateField(blank=True, null=True, verbose_name='Date de décès')),
            ],
        ),
        migrations.CreateModel(
            name='Editeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="Nom de l'éditeur")),
                ('website', models.URLField(blank=True, verbose_name='Site internet')),
                ('phone', models.CharField(blank=True, max_length=18, verbose_name='Téléphone')),
                ('adresse', models.CharField(blank=True, max_length=200, verbose_name='Adresse')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(blank=True, max_length=100, null=True, verbose_name='Genre du livre')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reserved', models.BooleanField(default=False, verbose_name='Réservé ?')),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nom')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('photo', models.URLField(blank=True, verbose_name='Photo')),
                ('adresse', models.CharField(blank=True, max_length=200, verbose_name='Adresse')),
                ('phone', models.CharField(blank=True, max_length=18, verbose_name='Téléphone')),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200, verbose_name='Titre du livre')),
                ('available', models.BooleanField(default=True, verbose_name='Disponneble ?')),
                ('publication', models.DateField(verbose_name='Date de publication')),
                ('couverture', models.URLField(blank=True, verbose_name='Image de courverture')),
                ('resume', models.TextField(blank=True, verbose_name='Résumé')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KIOSQUE.Auteur')),
                ('editeur', models.ManyToManyField(related_name='livres', to='KIOSQUE.Editeur')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KIOSQUE.Genre')),
            ],
        ),
    ]
