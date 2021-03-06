# Generated by Django 3.0.6 on 2020-05-22 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField(max_length=50)),
                ('email', models.TextField(max_length=50)),
                ('adresse', models.TextField(max_length=50)),
                ('telephone', models.TextField(max_length=50)),
            ],
            options={
                'verbose_name': 'fournisseur',
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.TextField(max_length=50)),
                ('categorie', models.TextField(max_length=50)),
                ('date', models.TextField(max_length=50)),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MiniProjetDjango.Fournisseur')),
            ],
            options={
                'verbose_name': 'medicament',
                'ordering': ['date'],
            },
        ),
    ]
