from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', 'recipieoptimizer.views.index', name='home'),
	url(r'^about/$', 
		TemplateView.as_view(template_name='about.html'),
		name='about'),
	url(r'^contact/$', 
		TemplateView.as_view(template_name='contact.html'),
		name='contact'),
	url(r'^recipes/(?P<slug>[-\w]+)/edit/$', 
		'recipieoptimizer.views.recipe_detail',
		name='recipe_detail'),
	url(r'^recipes/(?P<slug>[-\w]+)/$', 
		'recipieoptimizer.views.edit_recipe',
		name='edit_recipe'),
    url(r'^admin/', include(admin.site.urls)),
]
