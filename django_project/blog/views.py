from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post

    #2. by default, Django is gonna look for <app>/<model>_<viewtype>.html which is out case should be blog/post_list.html .. since we have another template for that, we can tell Django:
    template_name = 'blog/home.html'


def about(request):
    return render(request, 'blog/about.html')