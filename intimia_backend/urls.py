"""
URL configuration for intimia_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register(r'product', ProductViewSet, basename='Product')
# router.register(r'image', ImageViewSet, basename='Image')
# from reviews.views import ProductViewSet, ImageViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('user_module.urls')),
    path('api/v1/grossesse/', include('grossesse.urls')),
    path('api/v1/blog/', include('blog.urls')),
]+static(settings.STATIC_URL,documenmt_root = settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

liste=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
