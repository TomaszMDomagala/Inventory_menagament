from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
        )
from django.template import loader

from .models import FoodType

def index(request):
    latest_food_added = FoodType.objects.order_by('add_date')[:]
    template = loader.get_template('foods/index.html')
    context = {
        'latest_food_added' : latest_food_added,
        'title' : 'foods'
    }
    return HttpResponse(template.render(context, request))

class PostListView(ListView):
    model = FoodType
    template_name = 'foods/index.html'
    context_object_name = 'latest_food_added'
    ordering = ['-add_date']
    paginate_by = 20

class UserPostListView(ListView):
    model = FoodType
    template_name = 'foods/user_index.html'
    context_object_name = 'latest_food_added'
    ordering = ['-add_date']
    paginate_by = 20

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = FoodType

class PostCreateView(LoginRequiredMixin, CreateView):
    model = FoodType
    fields = ['food', 'add_date', 'exp_date', 'opened', 'opened_date', 'quantity', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = FoodType
    fields = ['exp_date', 'opened', 'opened_date', 'quantity']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = FoodType
    success_url = '/foods/'

    def test_func(self):
        foodtype = self.get_object()
        if self.request.user == foodtype.author:
            return True
        return False
