from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db.models import Q
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import P_Form
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post



def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'postbin/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'postbin/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

def post_list(request):
    queryset_list = Post.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list =  queryset_list.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query)
        ).distinct()
    context = {'posts': Post.objects.all()}
    return render(request, 'postbin/home.html', context)
    
class UserPostListView(ListView):
    model = Post
    template_name = 'postbin/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = P_Form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'postbin/about.html', {'title': 'About'})
