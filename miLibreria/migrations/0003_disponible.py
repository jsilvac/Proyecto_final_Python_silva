# Generated by Django 4.2.4 on 2023-08-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miLibreria', '0002_trabajador_remove_cliente_id_cli'),
    ]

    operations = [
        migrations.CreateModel(
            name='disponible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN_libro', models.CharField(max_length=50)),
                ('is_disponible', models.BooleanField(verbose_name=True)),
            ],
        ),
    ]
