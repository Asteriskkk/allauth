from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect
from django.utils import decorators

# Create your views here.
def home(request):
    return HttpResponseRedirect("/accounts/login/")


@login_required()
def profile(request):
    return render(request,"profile.html",{})