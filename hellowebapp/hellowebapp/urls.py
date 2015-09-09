from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', 'recipeoptimizer.views.index', name='home'),
	url(r'^about/$', 
		TemplateView.as_view(template_name='about.html'),
		name='about'),
	url(r'^contact/$', 
		TemplateView.as_view(template_name='contact.html'),
		name='contact'),
	url(r'^recipes/(?P<slug>[-\w]+)/edit/$', 
		'recipeoptimizer.views.recipe_detail',
		name='recipe_detail'),
	url(r'^recipes/(?P<slug>[-\w]+)/$', 
		'recipeoptimizer.views.edit_recipe',
		name='edit_recipe'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
