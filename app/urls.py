from .views import *
from django.urls import path

urlpatterns = [
	path('', menu),
	path('create/', create),
	path('search/', search, name='search'),
	path('rubric/<int:rubric_id>', rubrics),
	path('<int:pk>', detail)
]