from django.urls import path
from .views import *

urlpatterns = [
    path("profile/update/",Profile_Update, name="profile_update"),
    path("profile/<int:pk>/",ProfileDetailView.as_view(),name="profile_detail"),
    path("profile/delete/",ProfileDeleteView,name="profile_delete"),
]



