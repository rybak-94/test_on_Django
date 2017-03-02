from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils import timezone
from django import forms
from .models import Post
from .models import Test
from .forms import PostForm
from .forms import TestForm
from .forms import LoginForm

@login_required(login_url='/login/')
def main(request):
    return render(request, 'main/main.html')

@login_required(login_url='/login/')
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'main/post_list.html', {'posts': posts})

@login_required(login_url='/login/')
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})

@login_required(login_url='/login/')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'main/post_edit.html', {'form': form})

@login_required(login_url='/login/')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'main/post_edit.html', {'form': form})

@login_required(login_url='/login/')
def test_list(request):
    tests = Test.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'main/test_list.html', {'tests': tests})

@login_required(login_url='/login/')
def test_detail(request, pk):
    test = get_object_or_404(Test, pk=pk)
    return render(request, 'main/test_detail.html', {'test' : test})

@login_required(login_url='/login/')
def test_new(request):
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.author = request.user
            test.published_date = timezone.now()
            test.save()
            return redirect('test_detail', pk=test.pk)
    else:
        form = TestForm()
    return render(request, 'main/test_edit.html', {'form': form})

@login_required(login_url='/login/')
def test_edit(request, pk):
    test = get_object_or_404(Test, pk=pk)
    if request.method == "POST":
        form = TestForm(request.POST, instance=test)
        if form.is_valid():
            test = form.save(commit=False)
            test.author = request.user
            test.published_date = timezone.now()
            test.save()
            return redirect('test_detail', pk=test.pk)
    else:
        form = TestForm(instance=test)
    return render(request, 'main/test_edit.html', {'form': form})

@login_required(login_url='/login/')
def data(request):
    return render(request, 'main/data.html')

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.get_user():
                login(request, form.get_user())
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login/")
