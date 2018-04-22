from django.shortcuts import render,get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import request
from django.views.generic import ListView, DetailView,  CreateView
from django.views import View

from .models import BlogPost
from .forms import NewBlogPostForm
# Create your views here.

class PostListView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blogpost_list.html'
    #paginate_by = 2

'''
class PostView(View):
    def get(self, year, month, day, post):
        post = get_object_or_404(Post,
                                 slug=post,
                                 status='published',
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day,
                                 )
        return render(request, 'board.html', {'post': post})
'''


class PostView(View):
    def get(self, request, pk):
        post = get_object_or_404(BlogPost, pk=pk)
        return render(request, 'post2.html', {'post': post})


class NewPostFormView(CreateView):
    form_class = NewBlogPostForm
    template_name = 'post_create.html'
    slug_field = 'slug'
    success_url = reverse_lazy('post_list')