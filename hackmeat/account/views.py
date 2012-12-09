
from django.template import RequestContext
from django.shortcuts import render_to_response


def processors(request):
    return render_to_response('account/processors.html',
                            {},
                            context_instance=RequestContext(request))


def signup_farmer(request):
    return render_to_response('account/signup_farmer.html',
                            {},
                            context_instance=RequestContext(request))


def signup_processor(request):
    return render_to_response('account/signup_processor.html',
                            {},
                            context_instance=RequestContext(request))


def processor(request):
    return render_to_response('account/processor.html',
                            {},
                            context_instance=RequestContext(request))
