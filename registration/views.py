from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext 
from django.shortcuts import render_to_response

from registration.forms import UserForm

from reviewclone.models import Review

def home(request, template_name="home.html"):
    if hasattr(request.user, 'pk'):
        return HttpResponseRedirect(reverse('dashboard')) 
    reviews = Review.objects.all().order_by('-created_at')[:5]
    return render_to_response(
        template_name,
        {
            'reviews': reviews,
        },
        context_instance=RequestContext(request)
    ) 

def signup(request, template_name="signup.html"):
    if hasattr(request.user, 'pk'):
        HttpResponseRedirect(reverse('dashboard')) 
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data.get('username'),
                form.cleaned_data.get('email'),
                form.cleaned_data.get('password'),
            )
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            return HttpResponseRedirect(reverse('after_signup')) 
    else:
        form = UserForm()
    return render_to_response(
        template_name,
        {
            'form': form,
        },
        context_instance=RequestContext(request)
    ) 

