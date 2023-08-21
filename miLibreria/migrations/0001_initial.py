# Generated by Django 4.2.4 on 2023-08-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_Cli', models.IntegerField(max_length=10000)),
                ('nombreCli', models.CharField(max_length=200)),
                ('correoCli', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='libreria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreLi', models.CharField(max_length=100)),
                ('autorLi', models.CharField(max_length=200)),
                ('categoriaLi', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=50)),
                ('disponible', models.BooleanField(verbose_name=False)),
            ],
        ),
    ]