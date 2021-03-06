# Generated by Django 3.0.5 on 2020-10-02 18:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='titles', to='api.Genre', verbose_name='жанр'),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, db_index=True, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(2020)], verbose_name='Год выпуска'),
        ),
    ]
