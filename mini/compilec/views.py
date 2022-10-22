# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from compilec.forms import SignUpForm

# Create your views here.

def home(request):
   return render(request, "home.html", {})

def about(request):
   return render(request, "about.html", {})

def acc(request):
   return render(request, "acc.html", {})

def logout(request):
   return render(request, "logout.html", {})

def contact(request):
   return render(request, "contact.html", {})

def compiler(request):
   return render(request, "compiler.html", {})

def programs(request):
   return render(request, "programs.html", {})

def index(request):
   return render(request, "index.html", {})



  
# sign up


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


   #notes starts here

#1-i
   
def i1(request):
   return render(request, "syllabus/unit1/comp/i1.html", {})

def i2(request):
   return render(request, "syllabus/unit1/comp/i2.html", {})

def i3(request):
   return render(request, "syllabus/unit1/comp/i3.html", {})

def i4(request):
   return render(request, "syllabus/unit1/comp/i4.html", {})

def i5(request):
   return render(request, "syllabus/unit1/comp/i5.html", {})

def i6(request):
   return render(request, "syllabus/unit1/comp/i6.html", {})

#1-ii

def ii1(request):
   return render(request, "syllabus/unit1/numb/ii1.html", {})


#1-iii

def iii1(request):
   return render(request, "syllabus/unit1/clang/iii1.html", {})

def iii2(request):
   return render(request, "syllabus/unit1/clang/iii2.html", {})

def iii3(request):
   return render(request, "syllabus/unit1/clang/iii3.html", {})

def iii4(request):
   return render(request, "syllabus/unit1/clang/iii4.html", {})

def iii5(request):
   return render(request, "syllabus/unit1/clang/iii5.html", {})

def iii6(request):
   return render(request, "syllabus/unit1/clang/iii6.html", {})

def iii7(request):
   return render(request, "syllabus/unit1/clang/iii7.html", {})


#1-iv

def iv1(request):
   return render(request, "syllabus/unit1/AOE/iv1.html", {})
