from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
<<<<<<< HEAD
]
=======
    path('post/<int:pk>/', views.post_detail, name='post_inhoud'),
]
>>>>>>> 3473de8e13734d37b0a85cd217659aa8fddd9499
