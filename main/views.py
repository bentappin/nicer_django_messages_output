from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages

def index(request):
    messages.info(request, 'This is an info message.')
    messages.info(request, 'This is another info message.')
    messages.success(request, 'This is a success message.')
    messages.warning(request, 'This is a warning message.')
    messages.error(request, 'This is an error message.')
    messages.error(request, 'This is another error message.')
    return render_to_response('index.html', {
        }, context_instance=RequestContext(request))