from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Build, Survivor, Item


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    login = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)


class AddBuildForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    survivors = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Survivor.objects.all(), to_field_name='name')
    required_items = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Item.objects.all(), to_field_name='name')
    recommended_items = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Item.objects.all(), to_field_name='name')
    always_avoid_items = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Item.objects.all(), to_field_name='name')

    class Meta:
        model = Build
        fields = ('name', 'description', 'survivors', 'required_items', 'recommended_items', 'always_avoid_items')
