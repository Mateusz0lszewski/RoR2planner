from django.shortcuts import render, redirect, HttpResponse
from django.views import (View)
from .forms import SignUpForm, AddBuildForm
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class MainPageView(View):
    def get(self, request):
        return render(request, "main-page.html")


class CatalogItemsView(View):
    def get(self, request):
        items_list = Item.objects.all().order_by('name')
        return render(request, "catalog-items.html", {'items_list': items_list})


class ItemView(View):
    def get(self, request, **kwargs):
        item_name = str(kwargs['name'])
        item = Item.objects.get(name=item_name)
        return render(request, "item.html", {'item': item})


class CatalogSurvivorsView(View):
    def get(self, request):
        survivors_list = Survivor.objects.all().order_by('name')
        return render(request, "catalog-survivors.html", {'survivors_list': survivors_list})


class SurvivorView(View):
    def get(self, request, **kwargs):
        survivor_name = str(kwargs['name'])
        survivor = Survivor.objects.get(name=survivor_name)
        ability = Ability.objects.all().filter(survivor_id=survivor_name)
        return render(request, "survivor.html", {'survivor': survivor, 'ability': ability})


class CatalogBuildsView(View):
    def get(self, request):
        builds_list = Build.objects.all()
        return render(request, "catalog-builds.html", {'builds_list': builds_list})


class BuildView(View):
    def get(self, request, **kwargs):
        build_id = int(kwargs['id'])
        build = Build.objects.get(id=build_id)
        must_have = build.required_items.all()
        recommended = build.recommended_items.all()
        always_avoid = build.always_avoid_items.all()
        return render(request, "build.html", {'build': build, 'must_have': must_have, 'recommended': recommended, 'always_avoid': always_avoid})


class AddBuildView(LoginRequiredMixin, View):
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


class RegisterView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/login')
