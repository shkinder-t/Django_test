# Generated by Django 3.1.1 on 2020-09-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]