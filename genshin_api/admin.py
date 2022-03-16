from django.contrib import admin
from .models import CharacterType, CharacterNation

# Register your models here.
admin.site.register(CharacterType)
admin.site.register(CharacterNation)