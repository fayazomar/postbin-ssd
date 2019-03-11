from django.shortcuts import render

posts = [
    {
        'author': 'Fayaz Omar',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'November 1, 2018'
    },
    {
        'author': 'Abbas Ali',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'November 2, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'postbin/home.html', context)


def about(request):
    return render(request, 'postbin/about.html', {'title': 'About'})
