from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('upload/', views.upload, name='upload'),
    path('update/<str:pk>/', views.updateForm, name='updateForm'),
    path('delete/<str:pk>/', views.deleteForm, name='deleteForm'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

