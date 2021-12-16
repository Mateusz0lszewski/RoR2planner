import random
from django.shortcuts import render, redirect, HttpResponse
from django.views import (View)
from .forms import SignUpForm, AddBuildForm
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class MainPageView(View):
    """
    Displays main page of the site.
    """
    def get(self, request):
        builds = list(Build.objects.all())
        random_build = random.choice(builds)
        must_have = random_build.required_items.all()
        recommended = random_build.recommended_items.all()
        always_avoid = random_build.always_avoid_items.all()
        return render(request, "main-page.html", {'random_build': random_build, 'must_have': must_have, 'recommended': recommended, 'always_avoid': always_avoid})


class CatalogItemsView(View):
    """
    Displays catalog of items available in game.
    """
    def get(self, request):
        items_list = Item.objects.all().order_by('name')
        return render(request, "catalog-items.html", {'items_list': items_list})


class ItemView(View):
    """
    Displays details of specific item.
    """
    def get(self, request, **kwargs):
        item_name = str(kwargs['name'])
        item = Item.objects.get(name=item_name)
        return render(request, "item.html", {'item': item})


class CatalogSurvivorsView(View):
    """
    Displays catalog of survivors available in game.
    """
    def get(self, request):
        survivors_list = Survivor.objects.all().order_by('name')
        return render(request, "catalog-survivors.html", {'survivors_list': survivors_list})


class SurvivorView(View):
    """
    Displays details of specific hero.
    """
    def get(self, request, **kwargs):
        survivor_name = str(kwargs['name'])
        survivor = Survivor.objects.get(name=survivor_name)
        ability = Ability.objects.all().filter(survivor_id=survivor_name)
        return render(request, "survivor.html", {'survivor': survivor, 'ability': ability})


class AbilityView(View):
    """
    Displays details of specific ability.
    """
    def get(self, request, **kwargs):
        survivor_name = str(kwargs['s_name'])
        ability_name = str(kwargs['a_name'])
        survivor = Survivor.objects.get(name=survivor_name)
        ability = Ability.objects.get(name=ability_name)
        if ability.survivor_id == survivor_name:
            return render(request, "ability.html", {'survivor': survivor, 'ability': ability})


class CatalogMonsterView(View):
    """
    Displays catalog of monsters available in game.
    """
    def get(self, request):
        monsters_list = Monster.objects.all().order_by('name')
        return render(request, "catalog-monsters.html", {'monsters_list': monsters_list})


class MonsterView(View):
    """
    Displays details of specific monster.
    """
    def get(self, request, **kwargs):
        monster_name = str(kwargs['name'])
        monster = Monster.objects.get(name=monster_name)
        return render(request, "monster.html", {'monster': monster})


class CatalogBuildsView(View):
    """
    Displays catalog of builds created by community.
    """
    def get(self, request):
        builds_list = Build.objects.all()
        return render(request, "catalog-builds.html", {'builds_list': builds_list})


class BuildView(View):
    """
    Displays details of specific build.
    """
    def get(self, request, **kwargs):
        build_id = int(kwargs['id'])
        build = Build.objects.get(id=build_id)
        must_have = build.required_items.all()
        recommended = build.recommended_items.all()
        always_avoid = build.always_avoid_items.all()
        return render(request, "build.html", {'build': build, 'must_have': must_have, 'recommended': recommended, 'always_avoid': always_avoid})


class AddBuildView(LoginRequiredMixin, View):
    """
    Allows registered user to create new build.
    """
    def get(self, request):
        form = AddBuildForm()
        return render(request, 'add-build.html', {'form': form})

    def post(self, request):
        form = AddBuildForm(request.POST)
        build = Build()
        if form.is_valid():
            build.creator = request.user
            build.name = form.cleaned_data['name']
            build.description = form.cleaned_data['description']
            build.save()
            build.survivors.set(form.cleaned_data['survivors'])
            build.required_items.set(form.cleaned_data['required_items'])
            build.recommended_items.set(form.cleaned_data['recommended_items'])
            build.always_avoid_items.set(form.cleaned_data['always_avoid_items'])
            build.save()
            return redirect(f'/builds/{build.id}')

        else:
            return HttpResponse('Uzupełnij wszystkie dane!')


class EditBuildView(LoginRequiredMixin, View):
    """
    Allows registered user to edit their build.
    """
    def get(self, request, build_id):
        build = Build.objects.get(id=build_id)
        form = AddBuildForm(instance=build)
        return render(request, "add-build.html", {'build': build, 'form': form})

    def post(self, request, build_id):
        form = AddBuildForm(request.POST)
        build = Build()
        if form.is_valid():
            build.id = build_id
            build.creator = request.user
            build.name = form.cleaned_data['name']
            build.description = form.cleaned_data['description']
            build.survivors.set(form.cleaned_data['survivors'])
            build.required_items.set(form.cleaned_data['required_items'])
            build.recommended_items.set(form.cleaned_data['recommended_items'])
            build.always_avoid_items.set(form.cleaned_data['always_avoid_items'])
            return redirect(f'/builds/{build.id}')

        else:
            return HttpResponse('Uzupełnij wszystkie dane!')


class RegisterView(View):
    """
    Lets user sign in.
    """
    def get(self, request):
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/login')
