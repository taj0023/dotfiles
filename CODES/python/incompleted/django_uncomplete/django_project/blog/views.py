from django.shortcuts import render
# Create your views here.
posts = [
	{
		"author": "Thenga",
		"title": "This is the title",
		"date_posted": "oct 15"
	},
	{
		"author": "Kola",
		"title": "This is sometimes the title",
		"date_posted": "oct 11 "
	}
]

def home(request):
	context = {
		"posts": posts
	}
	return render(request, 'blog/home.html', context)
	
def about(request):
	return render(request, 'blog/about.html', {"title": "about"})