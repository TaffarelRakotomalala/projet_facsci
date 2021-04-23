# Generated by Django 3.1.7 on 2021-04-21 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210421_1230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note_user',
            old_name='NomMat',
            new_name='Nom_Mat',
        ),
        migrations.RenameField(
            model_name='note_user',
            old_name='NoteUser',
            new_name='Note_User',
        ),
        migrations.AddField(
            model_name='note_user',
            name='Poids_Mat',
            field=models.FloatField(max_length=10, null=True, verbose_name='Poids Matieres'),
        ),
        migrations.AddField(
            model_name='note_user',
            name='Validadation_UE',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='note_user',
            name='Validadation_semestre',
            field=models.BooleanField(default=False),
        ),
    ]
