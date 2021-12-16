from RoRplanner.models import *
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from django.contrib.auth.models import User
import pytest

# Create your tests here.


@pytest.mark.django_db
def test_item_model(item):
    assert len(Item.objects.all()) == 1
    assert Item.objects.get(name='Przedmiot1',
                            rarity=1,
                            description='abcxyz') == item


@pytest.mark.django_db
def test_survivor_model(survivor):
    assert len(Survivor.objects.all()) == 1
    assert Survivor.objects.get(name='Ocalały1',
                                description='xyz',
                                health=100,
                                health_regen=20.0,
                                damage=8.5,
                                speed=10,
                                armor=0.3,
                                image='portret.png') == survivor


@pytest.mark.django_db
def test_ability_model(ability, survivor):
    assert len(Ability.objects.all()) == 1
    assert Ability.objects.get(name='Umiejętność1',
                               description='xyz',
                               proc_coefficient=1.0,
                               cooldown=10,
                               type=2,
                               survivor=survivor) == ability


@pytest.mark.django_db
def test_monster_model(monster):
    assert len(Monster.objects.all()) == 1
    assert Monster.objects.get(name='Potwór1',
                               description='xyz',
                               health=100,
                               damage=8.5,
                               speed=10,
                               image='portret.png') == monster


"""
@pytest.mark.django_db
def test_build_model(build, survivor, item, user):
    assert len(Build.objects.all()) == 1
    assert Build.objects.get(id=1,
                             name='Kompozycja1',
                             description='xyz',
                             survivor=survivor,
                             required_items=item,
                             recommended_items=item,
                             always_avoid_items=item,
                             creator=user,
                             created='2021-12-12') == build
"""


@pytest.mark.django_db
def test_monster_model(monster):
    assert len(Monster.objects.all()) == 1
    assert Monster.objects.get(name='Potwór1',
                               description='xyz',
                               health=100,
                               damage=8.5,
                               speed=10,
                               image='portret.png') == monster


def test_main_page_view(client):
    response = client.get('/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'main-page.html')


@pytest.mark.django_db
def test_catalog_items_view(client):
    response = client.get('/items/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'catalog-items.html')
    assert len(response.context['items_list']) == Item.objects.all().count()


@pytest.mark.django_db
def test_item_view(client, item):
    response = client.get(f'/items/{item.name}/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'item.html')
    assert response.context['item'].name == 'Przedmiot1'
    assert response.context['item'].rarity == 1
    assert response.context['item'].description == 'abcxyz'
    assert response.context['item'].image == 'obrazek.png'


@pytest.mark.django_db
def test_catalog_survivors_view(client):
    response = client.get('/survivors/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'catalog-survivors.html')
    assert len(response.context['survivors_list']) == Survivor.objects.all().count()


@pytest.mark.django_db
def test_survivor_view(client, survivor, ability):
    response = client.get(f'/survivors/{survivor.name}/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'survivor.html')
    assert response.context['survivor'].name == 'Ocalały1'
    assert response.context['survivor'].description == 'xyz'
    assert response.context['survivor'].health == 100
    assert response.context['survivor'].health_regen == 20.0
    assert response.context['survivor'].damage == 8.5
    assert response.context['survivor'].speed == 10
    assert response.context['survivor'].armor == 0.3
    assert response.context['survivor'].image == 'portret.png'
    ability = Ability.objects.get(survivor=survivor)
    assert ability.name == 'Umiejętność1'
    assert ability.survivor == survivor


@pytest.mark.django_db
def test_catalog_monsters_view(client):
    response = client.get('/monsters/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'catalog-monsters.html')
    assert len(response.context['monsters_list']) == Monster.objects.all().count()


@pytest.mark.django_db
def test_monster_view(client, monster):
    response = client.get(f'/monsters/{monster.name}/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'monster.html')
    assert response.context['monster'].name == 'Potwór1'
    assert response.context['monster'].description == 'xyz'
    assert response.context['monster'].health == 100
    assert response.context['monster'].damage == 8.5
    assert response.context['monster'].speed == 10
    assert response.context['monster'].image == 'portret.png'


"""
@pytest.mark.django_db
def test_catalog_survivors_view(client):
    response = client.get('/survivors/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'catalog-survivors.html')
    assert len(response.context['survivors_list']) == Survivor.objects.all().count()


@pytest.mark.django_db
def test_survivor_view(client, survivor, ability):
    response = client.get(f'/survivors/{survivor.name}/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'survivor.html')
    assert response.context['survivor'].name == 'Ocalały1'
    assert response.context['survivor'].description == 'xyz'
    assert response.context['survivor'].health == 100
    assert response.context['survivor'].health_regen == 20.0
    assert response.context['survivor'].damage == 8.5
    assert response.context['survivor'].speed == 10
    assert response.context['survivor'].armor == 0.3
    assert response.context['survivor'].image == 'portret.png'
    ability = Ability.objects.get(survivor=survivor)
    assert ability.name == 'Umiejętność1'
    assert ability.survivor == survivor
"""

"""
@pytest.mark.django_db
def test_register_view(client):
    response = client.post("/register/",
                           {"login": "Użytkownik1",
                            "password": "BardzoTrudneHasło1",
                            "password2": "BardzoTrudneHasło1",
                            "first_name": "Imię1",
                            "last_name": "Nazwisko1",
                            "email": "email1@email.com"})
    assert response.status_code == 302


@pytest.mark.django_db
def test_login_view(client, user):
    response = client.post('/login/',
                           {'login': 'Użytkownik1',
                            'password': 'BardzoTrudneHasło1'})
    assert response.status_code == 200
"""