from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Author, Category, CreateBlog, Comment
from .forms import *
from rest_framework.response import Response
from rest_framework import views, status
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET'])
def getPostDetails(request, slug):
    post = get_object_or_404(CreateBlog, slug=slug)
    category = post.category  # Récupérer la catégorie associée au blog
    category_data = {
        "name": category.nom,
        "slug": category.slug
    }
    response = {
        "title": post.title,
        "excerpt": post.intro,
        "featuredImage": {
            "url": post.image.url
        },
        "author": {
            "name": post.author.nom,
            "bio": post.author.bio,
            "photo": {
                "url": post.author.photo.url
            }
        },
        "createdAt": post.date_added,
        "slug": post.slug,
        "content": {
            "html": post.body
        },
        "category": category_data
    }
    return JsonResponse(response)





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
            'photo':image_url2,'slug':post.slug,
            'categorie':post.category.nom,'createdAt':post.date_added})
        return Response(data)
    return Response({'error': 'Erreur lors de la requête'}, status=400)

   
@api_view(['GET'])
def getCategories(request):
     if request.method == "GET":
        category = Category.objects.all()
        data = {'category': []}
        for cat in category:
            data['category'].append({'title': cat.nom,  'slug':cat.slug})
        return Response(data)
     return Response({'error': 'Erreur lors de la requête'}, status=400)

@api_view(['GET'])
def getSimilarPosts(request, categories, slug):
    if request.method == "GET":
        posts = CreateBlog.objects.exclude(slug=slug).filter(category__slug__in=categories)[:3]
        return Response(posts.values())  
    return Response('echec', status=400) 


@api_view(['GET'])
def getRecentPosts(request):
    if request.method == "GET":
        posts = CreateBlog.objects.order_by('date_added').reverse()[:3]
        return Response(posts.values())  # Renvoyer les données brutes du QuerySet
    return Response('echec', status=400)  # Renvoyer une réponse avec un statut d'erreur approprié


# def getPostDetails(request, slug):
#     post = get_object_or_404(CreateBlog, slug=slug)
#     # Faites d'autres opérations avec l'objet `post` si nécessaire

#     # Retournez une réponse appropriée, par exemple :
#     return HttpResponse(f"Details of post with slug '{slug}'")


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

