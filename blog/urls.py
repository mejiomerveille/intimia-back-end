from django.urls import path
from blog.views import *

urlpatterns = [
    path('posts/recent/', getRecentPosts, name='get_recent_posts'),
    path('posts/', getPosts, name='get_posts'),
    path('categories/', getCategories, name='get_categories'),
    path('posts/<slug:slug>', getPostDetails, name='get_post_details'),
    path('posts/similar/', getSimilarPosts, name='get_similar_posts'),
    path('posts/adjacent/<createdAt>/<slug>/', getAdjacentPosts, name='get_adjacent_posts'),
    path('category/<slug>/', getCategoryPost, name='get_category_post'),
    path('posts/featured/', getFeaturedPosts, name='get_featured_posts'),
    path('comments/submit/', submitComment, name='submit_comment'),
    path('comments/<slug>/', getComments, name='get_comments'),

]