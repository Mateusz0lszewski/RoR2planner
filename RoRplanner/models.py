from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    RARITY = (
        (1, "Common"),
        (2, "Uncommon"),
        (3, "Legendary"),
        (4, "Boss"),
        (5, "Lunar"),
        (6, "Equipment")
    )
    rarity = models.SmallIntegerField(choices=RARITY)
    description = models.TextField()
    image = models.ImageField()
    '''
    stacking_stats = models.IntegerField
    STACKING = (
        (1, "linear"),
        (2, "hyperbolic"),
        (3, "exponential"),
        (4, "special"),
    )
    stacking_type = models.SmallIntegerField(choices=STACKING)
    '''

    def __str__(self):
        return self.name


class Survivor(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    description = models.TextField()
    health = models.FloatField()
    health_regen = models.FloatField()
    damage = models.FloatField()
    speed = models.FloatField()
    armor = models.FloatField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class Ability(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    description = models.TextField()
    proc_coefficient = models.FloatField(blank=True, null=True)
    cooldown = models.FloatField(blank=True, null=True)
    TYPE = (
        (0, "Passive"),
        (1, "Primary"),
        (2, "Secondary"),
        (3, "Utility"),
        (4, "Special")
    )
    type = models.SmallIntegerField(choices=TYPE)
    survivor = models.ForeignKey(Survivor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Build(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    survivors = models.ManyToManyField(Survivor)
    required_items = models.ManyToManyField(Item, related_name="required_in_builds")
    recommended_items = models.ManyToManyField(Item, related_name="recommended_in_builds", blank=True)
    always_avoid_items = models.ManyToManyField(Item, related_name="always_avoid_in_builds", blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
