from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy
from django.db.models import Q
from .models import *
from .forms import *

def search(request):
	query = request.GET.get('q')
	object_list = Posts.objects.filter(Q(title__icontains=query))
	context = {
		'object_list':object_list
	}
	return render(request, 'search.html', context)

class Register(CreateView):
	form_class = QuoteUserRegistrationForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('register-success')

	def get_success_url(self):
		if not self.success_url:
			raise ImproperlyConfigured('NO url to redirect')
		return str(self.success_url)


def menu(request):
	posts = Posts.objects.all()
	rubric = Category.objects.all()
	context = {
		'posts':posts,
		'rubric':rubric,
	}
	return render(request, 'menu.html', context)

def rubrics(request, rubric_id):
	posts = Posts.objects.filter(category=rubric_id)
	rubric = Category.objects.all()
	context = {
		'posts':posts,
		'rubric':rubric,
	}
	return render(request, 'rubric.html', context)

def detail(request, pk):
	post = Posts.objects.get(id=pk)
	rubric = Category.objects.all()
	context = {
		'post':post,
		'rubric':rubric,
	}
	return render(request, 'detail.html', context)

def create(request):
	form = PostsForm()
	if request.method == 'POST':
		form = PostsForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {
		'form':form
	}
	return render(request, 'create.html', context)


def edit(request, pk):
	pass

def delete(request, pk):
	pass