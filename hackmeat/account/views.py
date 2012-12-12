
from django.template import RequestContext
from django.shortcuts import render_to_response


def processors(request, zipcode=11201):
    return render_to_response('account/processors.html',
                            {
                                'zipcode': zipcode
                            },
                            context_instance=RequestContext(request))


def signup_farmer(request):
    return render_to_response('account/signup_farmer.html',
                            {},
                            context_instance=RequestContext(request))


def signup_processor(request):
    return render_to_response('account/signup_processor.html',
                            {},
                            context_instance=RequestContext(request))


def settings_farmer(request):
    return render_to_response('account/settings_farmer.html',
                            {},
                            context_instance=RequestContext(request))


def settings_processor(request):
    return render_to_response('account/settings_processor.html',
                            {},
                            context_instance=RequestContext(request))


def processor(request):
    return render_to_response('account/processor.html',
                            {},
                            context_instance=RequestContext(request))


def farmer(request):
    return render_to_response('account/farmer.html',
                            {},
                            context_instance=RequestContext(request))


def about(request):
    return render_to_response('base/about.html',
                            {},
                            context_instance=RequestContext(request))
