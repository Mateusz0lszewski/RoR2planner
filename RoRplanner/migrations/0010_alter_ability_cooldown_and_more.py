# Generated by Django 4.0 on 2021-12-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoRplanner', '0009_alter_ability_cooldown_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ability',
            name='cooldown',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ability',
            name='proc_coefficient',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
