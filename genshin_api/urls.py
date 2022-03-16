from django.urls import path, include
from .views import helloAPI

urlpatterns = [
	path("hello/", helloAPI),
	#path("charadata?id=<int:id>/", genshin_random_chara),
]