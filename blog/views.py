from django.shortcuts import get_object_or_404
from .models import Author, Category, CreateBlog, Comment
from .forms import *
from django.shortcuts import redirect, render
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework import views, status
from rest_framework.decorators import api_view

@api_view(['GET'])
def getPosts(request):
    if request.method == "GET":
        posts = CreateBlog.objects.all()
        data = {'posts': []}
        for post in posts:
            image_url = post.image.url if post.image else None
            image_url2 = post.author.photo.url if post.image else None
            data['posts'].append({'title': post.title, 'content': post.intro, 
            'image': image_url, 'name':post.author.nom,'bio':post.author.bio,
            'photo':image_url2,
            'categorie':post.category.nom})
        return Response(data)
    return Response({'error': 'Erreur lors de la requête'}, status=400)



def detailView(request, slug):
    post = CreateBlog.objects.get(slug=slug)
    comments = post.comments.all()
    paragraphs = post.body.splitlines()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.post = post
            form.save()
            return redirect('detailView', slug=post.slug)
    else:
        form = BlogForm()

    content = {
        'article':post,
        'comments':comments,
        'form':form,
        'paragraphs': paragraphs,

    }
    return render(request, 'blog/update.html', content)
    

def getCategories(request):
    return Category.objects.all()

def getPostDetails(request, slug):
    return get_object_or_404(CreateBlog, slug=slug)

def getSimilarPosts(categories, slug):
    return CreateBlog.objects.exclude(slug=slug).filter(category__slug__in=categories)[:3]

def getAdjacentPosts(createdAt, slug):
    next_post = CreateBlog.objects.filter(createdAt__gt=createdAt).exclude(slug=slug).order_by('createdAt').first()
    previous_post = CreateBlog.objects.filter(createdAt__lt=createdAt).exclude(slug=slug).order_by('-createdAt').first()
    return {'next': next_post, 'previous': previous_post}

def getCategoryPost(slug):
    category = get_object_or_404(Category, slug=slug)
    return CreateBlog.objects.filter(category=category)

def getFeaturedPosts():
    return CreateBlog.objects.filter(featuredPost=True)

def submitComment(obj):
    post = get_object_or_404(CreateBlog, slug=obj['slug'])
    comment = Comment(post=post, email=obj['email'], body=obj['body'], name=obj['name'])
    comment.save()
    return comment

def getComments(slug):
    post = get_object_or_404(CreateBlog, slug=slug)
    return Comment.objects.filter(post=post)

def getRecentPosts():
    return CreateBlog.objects.order_by('date_added').reverse()[:3]

