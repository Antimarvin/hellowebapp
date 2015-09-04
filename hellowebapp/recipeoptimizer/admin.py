from django.contrib import admin
from recipieoptimizer.models import Recipe
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
	model = Recipe
	list_display = ('name', 'description',)
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Recipe, RecipeAdmin)