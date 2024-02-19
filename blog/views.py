from datetime import datetime
from django.views import View
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Author, Category, CreateBlog, Comment
from .forms import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.request import Request

class CategoryPostView(View):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        posts = CreateBlog.objects.filter(category=category).values()
        # Convertir le QuerySet en une liste de dictionnaires
        posts_list = list(posts)
        return JsonResponse(posts_list, safe=False)

@api_view(['GET'])
def getPostDetails(request, slug):
    post = get_object_or_404(CreateBlog, slug=slug)
    categories = post.category  
    category_data = {
        "name": categories.nom,
        "slug": categories.slug
    }
    content_data = post.body if post.body else ""
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
        "content":(content_data).splitlines()  ,
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
            'image': image_url,
             'author':{
             'name':post.author.nom,'bio':post.author.bio,
            'photo':image_url2,},'slug':post.slug,
            'categorie':post.category.nom,'date_added':post.date_added})
        return JsonResponse(data)
    return Response({'error': 'Erreur lors de la requête'}, status=400)

   
@api_view(['GET'])
def getCategories(request):
     if request.method == "GET":
        categories = Category.objects.all()
        data = {'category': []}
        for cat in categories:
            data['category'].append({'title': cat.nom,  'slug':cat.slug})
        return Response(data)
     return Response({'error': 'Erreur lors de la requête'}, status=400)


@api_view(['GET'])
def getSimilarPosts(request):
    if request.method == "GET":
        # posts = CreateBlog.objects.filter(category=categories).values('category')
        categories = request.GET.getlist('categories')  
        semaine=request.GET.get('semaine')
        slug = request.GET.get('slug')
        print(categories)
        # print(posts)
        if categories and slug:
            posts = CreateBlog.objects.exclude(slug=slug).filter(category__slug__in=categories)[:3]
            return Response(posts.values())  
        else:
            return Response('Categories and slug parameters are required.', status=400)


@api_view(['GET'])
def getRecentPosts(request):
    if request.method == "GET":
        posts = CreateBlog.objects.order_by('date_added').reverse()[:3]
        return Response(posts.values())  
    return Response('echec', status=400)  
from datetime import timedelta

def getAdjacentPosts(request,date_added:str):
    print(f"date recu est {date_added}")
    date_added_str = datetime.now().isoformat()
    if date_added.isdigit():
        if len(date_added)>9:
           date_added = int(date_added)/1000 if len(date_added)> 10 else float(date_added)
           date_convert = datetime.fromtimestamp(date_added) #+ timedelta(hours=1)
           print(f"date recu est {date_added}")
           date_added_str = date_convert.isoformat()
    next_post = CreateBlog.objects.filter(date_added__gt=date_added_str).order_by('date_added').values('FeaturePost', 'author', 'author_id', 'body', 'category', 'category_id', 'comments', 'date_added', 'image', 'intro', 'title') or None
    previous_post = CreateBlog.objects.filter(date_added__lt=date_added_str).order_by('-date_added').values('FeaturePost', 'author', 'author_id', 'body', 'category', 'category_id', 'comments', 'date_added', 'image', 'intro', 'title') or None
    np = next_post[0] if next_post is not None else None
    pp = previous_post[0] if previous_post is not None else None
    response_data = {'next':  np, 'previous': pp}
    return JsonResponse(response_data)


@api_view(['GET'])
def getFeaturedPosts(request):
    if request.method == "GET":
        posts = CreateBlog.objects.all()
        data = {'posts': []}
        for post in posts:
            image_url = post.image.url if post.image else None
            image_url2 = post.author.photo.url if post.image else None
            data['posts'].append({'title': post.title, 
            'image': image_url, 'name':post.author.nom,'bio':post.author.bio,
            'photo':image_url2,'slug':post.slug,'date':post.date_added,
            })
        return Response(data)
    return Response({'error': 'Erreur lors de la requête'}, status=400)

@api_view(['POST'])
def submitComment(request):
    post = get_object_or_404(CreateBlog, slug=request.data['slug'])

    # Pré-remplir les champs `name` et `email` avec les informations de l'utilisateur connecté
    user = request.user

    comment = Comment(
        post=post,
        email=user.email,
        name=user.username,
        body=request.data['comment'],
    )
    comment.save()

    request.data['id'] = comment.pk
    return JsonResponse(request.data)

import json
@api_view(['GET'])
def getComments(request,slug=None):
    if slug  is not None:
        try:
            post = CreateBlog.objects.get(slug=slug)
            comment=Comment.objects.filter(post=post).values('id','email','name','body','date_added')
        except Exception as e:
            print(e)
            return Response(None)
    else:
        comment=Comment.objects.filter().values('id','email','name','body','date_added')
    # print(f"comment simple {list(comment)}")
    # print(request)
    return Response(json.dumps(list(comment), cls=DjangoJSONEncoder))