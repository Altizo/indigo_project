from django.urls import path
from . import views

urlpatterns = [
    path('all', views.all, name='price_All'),
    path('press', views.press, name='price_Press'),
    path('brending', views.brending, name='price_brending'),
    path('razmeshenie', views.razm, name='price_razm'),
    path('web', views.web, name='price_web'),
    path('design', views.design, name='price_Design')
]
