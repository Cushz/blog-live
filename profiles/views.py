from webbrowser import get
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import ProfileUpdateForm, UserUpdateForm
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def Profile_Update(request):# Function based qurmaq daha rahat oldu hemde basha dushulen. Ona gore bu function based view oldu
    if request.method  == "POST":
        user_form = UserUpdateForm(request.POST,instance = request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile has been updated!')
            return redirect("home")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance = request.user.profile)
    
    context = {
        "user_form" : user_form,
        "profile_form": profile_form,
    }
    return render(request,'update.html',context)

@login_required
def ProfileDeleteView(request):
    user = User.objects.get(username=request.user)
    user.delete()
    return redirect("login")

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "detail.html"
    context_object_name = "profile"
# def Profile_detail(request,id):
#     context ={}
#     context["profile"] = Profile.objects.get(id=id)
#     return render(request,"detail.html",context)
# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = Profile
#     form_class = ProfileUpdateForm
#     template_name = "update.html"
#     def get_success_url(self):
#         messages.success(self.request,'Profile has been updated!')
#         return reverse_lazy("login")
        #Use only form class or fields. Do not use both of them at the same time