# Generated by Django 4.1.4 on 2023-01-02 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='mail',
            field=models.EmailField(max_length=100, verbose_name='enail'),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='password',
            field=models.CharField(max_length=100, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='phone'),
        ),
    ]
