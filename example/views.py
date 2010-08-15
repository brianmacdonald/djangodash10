from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext 
from django.shortcuts import render_to_response

from example.forms import UserForm

def signup(request, template_name="signup.html"):
    if hasattr(request.user, 'pk'):
        HttpResponseRedirect(reverse('dashboard')) 
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()                                      
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

