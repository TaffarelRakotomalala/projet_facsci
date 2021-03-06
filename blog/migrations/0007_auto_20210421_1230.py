# Generated by Django 3.1.7 on 2021-04-21 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20210421_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semestre', models.CharField(choices=[('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6'), ('S7', 'S7'), ('S8', 'S8'), ('S9', 'S9'), ('S10', 'S10')], max_length=3)),
                ('Nom_UE', models.CharField(max_length=20, verbose_name="Unité d'enseignement")),
                ('NomMat', models.CharField(max_length=30, verbose_name='Matieres')),
                ('NoteUser', models.FloatField(max_length=10, verbose_name='Note')),
                ('Us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="L'étudiant")),
            ],
        ),
        migrations.AlterModelOptions(
            name='profil',
            options={'ordering': ['utilisateur']},
        ),
        migrations.DeleteModel(
            name='Unite_Ens',
        ),
    ]
