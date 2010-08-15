from django.contrib import messages  
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext 

def signup(request, template_name="signup.html"):
    if request.user.pk:
        HttpResponseRedirect(reverse('dashboard')) 
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 
                                'Your account has been created')
            return HttpResponseRedirect(reverse('dashboard')) 
    else:
        form = RegisterForm()
    return render_to_response(
        template_name,
        {
            'form': form,
        },
        context_instance=RequestContext(request)
    ) 

