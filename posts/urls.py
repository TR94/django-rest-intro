from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view()), 
    # we call as_view because its a class based view - see views.py
]