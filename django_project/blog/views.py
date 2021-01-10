from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
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

class PostCreatelView(LoginRequiredMixin, CreateView):
    # Note:
    # This one will share a template with the update view 
    # by default, the template name for this view is to be the name of the model followed by underscore "form".. in our case, post_form.html
    # CreateView expected the form to be called "form"
    model = Post
    fields = ['title', 'content']

    # override form_valid method to pass the logged-in User
    def form_valid(self, form):
        # before submitting (validating) the form, take the instance and set its author to the current logged-in user  
        form.instance.author = self.request.user
        # validate the form by running the form_valid method on parent class
        return super().form_valid(form)


class PostUpdatelView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
        should use the same template as PostCreateView, i.e. post_form.html
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
            UserPassesTestMixin will run this function to handle unauthorized User access
        """
        # to get the exact post user wants to update, we use method of UpdateView
        post = self.get_object()
        # check if current User is Author of the post:
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        """
            UserPassesTestMixin will run this function to handle unauthorized User access
        """
        # to get the exact post user wants to update, we use method of UpdateView
        post = self.get_object()
        # check if current User is Author of the post:
        return self.request.user == post.author
def about(request):
    return render(request, 'blog/about.html')