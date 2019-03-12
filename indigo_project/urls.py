"""indigo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

if settings.DEBUG:
    urlpatterns = [
        path('', include('home.urls')),
        path('info/', include('info.urls')),
        path('about_us/', include('about_us.urls')),
        path('portfolio/', include('portfolio.urls')),
        path('price/', include('price.urls')),
        path('contact/', include('contact.urls')),
        path('*', include('coming_soon.urls')),
        path('admin/', admin.site.urls)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns = [
        path('', include('home.urls')),
        path('info/', include('info.urls')),
        path('about_us/', include('about_us.urls')),
        path('portfolio/', include('portfolio.urls')),
        path('price/', include('price.urls')),
        path('contact/', include('contact.urls')),
        path('*', include('coming_soon.urls')),
        path('admin/', admin.site.urls)
    ]


