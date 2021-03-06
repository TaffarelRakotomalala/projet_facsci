# Generated by Django 3.1.7 on 2021-03-31 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matieres',
            name='NomMat',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='matieres',
            name='Ue',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='MoyenneUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MoyenneMat', models.FloatField(max_length=10)),
                ('MoyenneTotal', models.FloatField(max_length=10)),
                ('UserMoy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
