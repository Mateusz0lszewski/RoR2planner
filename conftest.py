import pytest
from RoRplanner.models import *
from django.contrib.auth.models import User


@pytest.fixture
def user():
    return User.objects.create_user(
        username='Użytkownik1',
        password='BardzoTrudneHasło1',
        first_name='Imię1',
        last_name='Nazwisko1',
        email='email1@email.com'
    )


@pytest.fixture
def item():
    return Item.objects.create(
        name='Przedmiot1',
        rarity=1,
        description='abcxyz',
        image='obrazek.png'
    )


@pytest.fixture
def survivor():
    return Survivor.objects.create(
        name='Ocalały1',
        description='xyz',
        health=100,
        health_regen=20.0,
        damage=8.5,
        speed=10,
        armor=0.3,
        image='portret.png'
    )


@pytest.fixture
def ability(survivor):
    return Ability.objects.create(
        name='Umiejętność1',
        description='xyz',
        proc_coefficient=1.0,
        cooldown=10,
        type=2,
        survivor=survivor
        )


@pytest.fixture
def monster():
    return Monster.objects.create(
        name='Potwór1',
        description='xyz',
        health=100,
        damage=8.5,
        speed=10,
        image='portret.png'
    )


"""
@pytest.fixture
def build(survivor, item, user):
    return Build.objects.create(
        id=1,
        name='Kompozycja1',
        description='xyz',
        survivors=Survivor.objects.filter(name=survivor.name),
        required_items=item,
        recommended_items=item,
        always_avoid_items=item,
        creator=user,
        created='2021-12-12'
        )
"""