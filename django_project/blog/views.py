from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    # which model to query to create the List View?
    # by convention, this is all what you need to get going..
    model = Post

    #2. by default, Django is gonna look for <app>/<model>_<viewtype>.html which is out case should be blog/post_list.html .. since we have another template for that, we can tell Django:
    template_name = 'blog/home.html'

    #3. by default, out list view is going to call variable object list. So either go to template and loop through object list, or we can set one more variable in our list view and let the class know that we want that variable to be called "post" instead.
    context_object_name = 'posts'

    #4. change order of displayed posts
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    # this is gonna be looking for blog/post_detail.html by default and expecting the context of this template to be called "object"

def about(request):
    return render(request, 'blog/about.html')