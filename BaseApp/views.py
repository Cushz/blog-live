from pipes import Template
from webbrowser import get

from django.http import HttpResponse
from .models import PostModel
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView 
from django.views.generic.edit import CreateView
from django.urls import reverse,reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import *
from profiles.models import *
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
# Create your views here.

class PostsListView(LoginRequiredMixin,ListView):
    template_name = "index.html"
    context_object_name = "post_list"
    paginate_by = 2
    queryset = PostModel.objects.all()
    
class SearchedPostView(LoginRequiredMixin,ListView):
    template_name = "post_search.html"
    model = PostModel
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = PostModel.objects.filter(title__icontains=query)
        else:
            object_list = PostModel.objects.none()
        return object_list
class PostsDetailView(LoginRequiredMixin,DetailView):
   model = PostModel
   template_name = "post_detail.html"
   context_object_name = "post"

# def LoginView(request): basha dushmey uchun function based de de qurmusham her ehtimala
#     form = LoginForm()
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password"])
#             if user is not None:
#                 login(request,user)
#                 messages.success(request,"Logged in successfully")
#                 return redirect("home")
#             else:
#                 messages.error(request,"Login Failed")
#     return render(request,"login.html",{"form":form})

class LoginView(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy("home")
    def dispatch(self, request, *args, **kwargs): # if user is authenticated, it is gonna prevent from login page
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)
    

class PostCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name = "post_create.html"
    model = PostModel
    fields = ["title","content"]
    def form_valid(self, form): # authomatically defines the author who publishes the post
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy("home")
    success_message = "New post has been added successfully"
class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    template_name = "post_update.html"
    model = PostModel
    fields = ["title","content"]
    def form_valid(self, form): # authomatically defines the author who publishes the post
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self): # used for userpassestestmixin to limit users to only edit their own posts
        prod = get_object_or_404(PostModel,pk = self.kwargs["pk"])
        return self.request.user == prod.author
    success_message = "Your post has been updated successfully"
    success_url = reverse_lazy("home")

class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    template_name = "post_delete.html"
    context_object_name = "post"
    success_message = "Your post has been deleted successfully"
    queryset = PostModel.objects.all()
    def test_func(self): # used for userpassestestmixin to limit users to only edit their own posts
        prod = get_object_or_404(PostModel,pk = self.kwargs["pk"])
        return self.request.user == prod.author
    success_url = reverse_lazy("home")

# def PostDeleteView(request, pk):
#     post = PostModel.objects.get(id=pk)
#     if request.method == 'POST':
#         post.delete()
#         messages.add_message(request, messages.INFO, 'Post Has been deleted')
#         return redirect("home")
#     return render(request,'post_delete.html',{'post': post})
   
# class RegisterView(SuccessMessageMixin,CreateView): it only created user not profile so i had to change to function based view
#     template_name = "register.html"
#     form_class = RegisterForm
#     success_url = reverse_lazy("login")
#     success_message = "Your profile has been created successfully"

def Profile_Register(request):
    form = RegisterForm()
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']          
            email = form.cleaned_data['email']
            password_one = form.cleaned_data['password1']
            password_two = form.cleaned_data['password2']

            user = User.objects.create_user(username=username,email=email,password=password_one)
            user.save()
            #add user profile
            user_profile = Profile(user=user)
            user_profile.save()
            messages.success(request,"Your profile has been created successfully")
            return redirect("login")
        else:
            context = {"form":form}
            return render(request,"login.html",context)
    context = {'form':form}
    return render(request,"register.html",context)
        

   
