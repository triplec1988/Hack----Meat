from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.shortcuts import redirect

import forms

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


def reservation(request):
    if request.method == 'POST':
        form = forms.ReservationForm(request.POST)
        if form.is_valid():
            print form.cleaned_data
            form = forms.CutForm(request.GET)
            return render_to_response('reservation/cut_step.html', {'form': form},context_instance=RequestContext(request))
    else:
        form = forms.ReservationForm()
        
    return TemplateResponse(request, 'reservation/reservation.html', {
            'form': form,
    })


def cut_step(request):
    if request.method == 'POST':
        form = forms.CutForm(request.POST)
        if form.is_valid():
            print form.cleaned_data
            
            return render_to_response('reservation/reservation_complete.html', {},context_instance=RequestContext(request))
    else:
        form = forms.CutForm()
        
    return TemplateResponse(request, 'reservation/cut_step.html', {
            'form': form,
    })


def reservation_complete(request):
    return TemplateResponse(request, 'reservation/reservation_complete.html')





