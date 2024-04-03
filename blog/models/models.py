from django.db import models
from django.db.models.fields.related import ForeignKey
from forfait.models import Forfait

class Author(models.Model):
    nom = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media')
    bio =models.CharField(max_length=255)

class Category(models.Model):
    nom =models.CharField(max_length=50)
    slug=models.SlugField(unique=True) 

class CreateBlog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    intro = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='media')
    FeaturePost=models.BooleanField(default=True)# s'affiche sur le slide si vrai  
    date_added = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    semaine = models.IntegerField(default=0)
    blog_forfait =models.ForeignKey(Forfait,on_delete=models.CASCADE,default=None,null=True)



    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = ForeignKey(CreateBlog, related_name='comments', on_delete=models.CASCADE)
    email = models.EmailField()
    body = models.TextField()
    name = models.CharField(max_length=100, default="inconnu")
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_added']