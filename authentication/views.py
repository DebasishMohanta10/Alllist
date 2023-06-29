from django.shortcuts import render
from .forms import LoginForm,RegisterForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse

class Login(LoginView):
    redirect_authenticated_user = True
    form_class = LoginForm
    template_name = 'authentication/login.html'

class Logout(LogoutView):
    pass

def signupView(request,template_name="authentication/signup.html"):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save()
        login(request,user)
        return HttpResponseRedirect(reverse('tasks_list'))
    context = {"form": form}
    return render(request,template_name,context)



