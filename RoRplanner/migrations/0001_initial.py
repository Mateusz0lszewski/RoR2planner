# Generated by Django 4.0 on 2021-12-07 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rarity', models.SmallIntegerField(choices=[(1, 'Common'), (2, 'Uncommon'), (3, 'Legendary'), (4, 'Boss'), (5, 'Lunar'), (6, 'Equipment')])),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
