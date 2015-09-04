from django.shortcuts import render, redirect
from recipieoptimizer.forms import RecipeForm
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
	
def edit_recipe(request, slug):
	#grab the object...
	recipe = Recipe.objects.get(slug=slug)
	# set the form we're using...
	form_class = RecipeForm
	# if we're coming to this view from a submitted form,
	if request.method == 'POST':
		# grab the data from the submitted form
		form = form_class(data=request.POST, instance=recipe)
		if form.is_valid():
			# save the new data
			form.save()
			return redirect('recipe_detail', slug=recipe.slug)
	
	#otherwise just create the form
	else:
		form = form_class(instance=recipe)
		
	return render(request, 'recipes/edit_recipe.html', {
		'recipe': recipe,
		'form': form,
	})