from django.template import RequestContext
from django.shortcuts import render_to_response

def search(request):
	return render_to_response('reservation/search.html',
							{},
							context_instance=RequestContext(request))

def processor_reserve(request):
	return render_to_response('reservation/processor_reserve.html',
							{},
							context_instance=RequestContext(request))

def order(request):
	return render_to_response('reservation/order.html',
							{},
							context_instance=RequestContext(request))


def confirmation(request):
	return render_to_response('reservation/confirmation.html',
							{},
							context_instance=RequestContext(request))
