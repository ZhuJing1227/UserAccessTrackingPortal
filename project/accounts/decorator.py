from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from .models import employee
from django.shortcuts import render,redirect

#check whether user already login
def already_login(view_func):
    def wrapper_func(request, *args, **kwargs):
        #if session exist,user is already login, will auto redirect to home
        if 'employeeName' in request.session:
            return redirect('home')
        #if no session, means user is not login, redirect to login page
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

#in case user did not login
def is_login(view_func):
    def wrapper_func(request, *args, **kwargs):
        #if session exist, it is ok, continue
        if 'employeeName' in request.session:
                return view_func(request, *args, **kwargs)
        #if session not exist, redirect to login
        else:
            return redirect('login')
    return wrapper_func

#check whether account can login
def can_login(view_func):
    def wrapper_func(request, *args, **kwargs):
        #check if session expire
        if 'employeeName' in request.session:
            #if is admin account, allow login
            if request.session['accountLevel'] == 'admin':
                return view_func(request, *args, **kwargs)
            #if is user account, allow login
            elif request.session['accountLevel'] == 'user':
                return view_func(request, *args, **kwargs)
            #else, not allowed
            else:
                messages.error(request,'You have no access to the system.')
                request.session.clear()
                return redirect('login')
        #if session expired, redirect to login page
        else:
            return redirect('login')
    return wrapper_func

#only allow admin to view the page
def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        #check whether account login
        if 'accountLevel' in request.session:
            #if account is admin, continue
            if request.session['accountLevel'] == 'admin':
                return view_func(request, *args, **kwargs)
            #else, error message and redirect to home
            else:
                messages.error(request,'You have no access to this page.')
                return redirect('home')
    return wrapper_func

#only allow user to view the page
def user_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        #check whether account login
        if 'accountLevel' in request.session:
            #if account is user, continue
            if request.session['accountLevel'] == 'user':
                return view_func(request, *args, **kwargs)
            #else, error message and redirect to home
            else:
                messages.error(request,'You have no access to this page.')
                return redirect('home')
    return wrapper_func

