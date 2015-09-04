from django.shortcuts import render
from recipieoptimizer.models import Recipe

# Create your views here.
def index(request):
	recipes = Recipe.objects.all()
	# this is your new view
	return render(request, 'index.html', {
		'recipes': recipes,
	})

def recipe_detail(request, slug):
	# grab the object...
	recipe = Recipe.objects.get(slug=slug)
	return render(request, 'recipes/recipe_detail.html', {
		'recipe': recipe,
	})