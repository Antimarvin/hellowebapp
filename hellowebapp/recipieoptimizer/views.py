from django.shortcuts import render

# Create your views here.
def index(request):
	number = 6
	name = "Ricky Sweat"
	# this is your new view
	return render(request, 'index.html', {
		'number': number,
		'name': name,
	})