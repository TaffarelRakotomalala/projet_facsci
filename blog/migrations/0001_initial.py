# Generated by Django 3.1.7 on 2021-05-05 14:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='inscription',
            fields=[
                ('Carte_etudiant', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name="Carte d'étudiant")),
                ('Nom', models.CharField(max_length=20)),
                ('Prenom', models.CharField(max_length=50, verbose_name='Prénom')),
                ('Mention', models.CharField(choices=[('MA', 'Mathematique et Application'), ('PC', 'Physique Chimie'), ('PA', 'Physique Application'), ('SV', 'Science de la vie')], help_text='Choisir votre mention', max_length=30)),
                ('Parcour', models.CharField(choices=[('MISS', 'MISS'), ('MF', 'MF'), ('ME', 'ME')], help_text='Choisir votre parcours', max_length=30)),
                ('mail', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^.{10}$')])),
                ('ouiounon', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_titre', models.CharField(max_length=200)),
                ('pub_contenu', models.TextField(blank=True, null=True)),
                ('pub_image', models.FileField(blank=True, null=True, upload_to='files')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcour', models.CharField(choices=[('MISS', 'MISS'), ('MF', 'MF'), ('ME', 'ME')], max_length=5, verbose_name='Choisissez Votre Parcours: ')),
                ('avatar', models.ImageField(blank=True, default='avatars/student_male_64px.png', null=True, upload_to='avatars/')),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Choisissez Votre CE: ')),
            ],
            options={
                'ordering': ['utilisateur'],
            },
        ),
        migrations.CreateModel(
            name='Note_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semestre', models.CharField(choices=[('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6'), ('S7', 'S7'), ('S8', 'S8'), ('S9', 'S9'), ('S10', 'S10')], max_length=3, null=True)),
                ('Nom_UE', models.CharField(max_length=20, null=True, verbose_name="Unité d'enseignement")),
                ('Nom_Mat', models.CharField(max_length=30, null=True, verbose_name='Matieres')),
                ('Note', models.FloatField(max_length=10, null=True, verbose_name='Note')),
                ('Poids_Mat', models.FloatField(max_length=10, null=True, verbose_name='Poids Matieres')),
                ('Validation_UE', models.BooleanField(default=False)),
                ('Validation_Semestre', models.BooleanField(default=False)),
                ('Us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="L'étudiant")),
            ],
        ),
        migrations.CreateModel(
            name='fichier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de ce jour')),
                ('mention', models.CharField(choices=[('MA', 'Mathematique et Application'), ('PC', 'Physique Chimie'), ('PA', 'Physique Application'), ('SV', 'Science de la vie')], max_length=100, verbose_name='Mention')),
                ('niveau', models.CharField(choices=[('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3'), ('M1', 'M1'), ('M2', 'M2')], max_length=100, verbose_name='Niveau')),
                ('matiers', models.CharField(max_length=100, verbose_name='Nom des matières')),
                ('desc', models.CharField(choices=[('Cours', 'Cours'), ('TD', 'TD'), ('TP', 'TP')], max_length=10, verbose_name='Cours ou TD')),
                ('fichiers', models.FileField(upload_to='fichiers/', verbose_name='Nom du fichier')),
                ('util', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="L'utilisateur")),
            ],
        ),
    ]
