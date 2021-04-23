# Generated by Django 3.1.7 on 2021-04-23 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_auto_20210421_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note_user',
            name='Nom_Mat',
            field=models.CharField(max_length=30, null=True, verbose_name='Matieres'),
        ),
        migrations.AlterField(
            model_name='note_user',
            name='Nom_UE',
            field=models.CharField(max_length=20, null=True, verbose_name="Unité d'enseignement"),
        ),
        migrations.AlterField(
            model_name='note_user',
            name='Note',
            field=models.FloatField(max_length=10, null=True, verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='note_user',
            name='Semestre',
            field=models.CharField(choices=[('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6'), ('S7', 'S7'), ('S8', 'S8'), ('S9', 'S9'), ('S10', 'S10')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='note_user',
            name='Us',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="L'étudiant"),
        ),
    ]