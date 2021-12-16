from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Item)
admin.site.register(Survivor)
admin.site.register(Build)
admin.site.register(Ability)
admin.site.register(Monster)
