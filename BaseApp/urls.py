from django.urls import reverse,path
from .views import *
urlpatterns = [
    path("",PostsListView.as_view(),name="home"),
    path("<int:pk>/",PostsDetailView.as_view(),name="post_detail"),
    path("login/",LoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(next_page="login"),name="logout"),
    path("register/",Profile_Register,name="register"),
    path("create/",PostCreateView.as_view(),name="post_create"),
    path("delete/<int:pk>/",PostDeleteView.as_view(),name="post_delete"),
    path("update/<int:pk>/",PostUpdateView.as_view(),name="post_update"),
    path("search/",SearchedPostView.as_view(),name="post_search"),
]
