from django.views.generic import (ListView, DetailView, CreateView,UpdateView)
from django.urls import reverse_lazy
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = '-date_post'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/new.html'
    context_object_name = 'new'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'
    success_url = reverse_lazy('post_list')

class PostSearch(ListView):
        model = Post
        ordering = '-date_post'
        template_name = 'post_search.html'
        context_object_name = 'news'
        paginate_by = 2

        def get_queryset(self):
            queryset = super().get_queryset()
            self.filterset = PostFilter(self.request.GET, queryset=queryset)
            return self.filterset.qs

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['filterset'] = self.filterset
            return context

class PostEdit(UpdateView):

    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')









   # Create your views here.
