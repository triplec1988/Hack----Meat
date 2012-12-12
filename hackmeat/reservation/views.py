from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.conf import settings

import mandrill
import logging

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
            form = forms.CutForm(request.POST)
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
            
            return redirect('reservation_complete')
    else:
        form = forms.CutForm()
        
    return TemplateResponse(request, 'reservation/cut_step.html', {
            'form': form,
    })


def reservation_complete(request):
    return TemplateResponse(request, 'reservation/reservation_complete.html')


def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            try:
                # send the contact information via Mandrill
                m = mandrill.Mandrill(settings.MANDRILL_API_KEY)
                m.messages.send({
                    'text': form.cleaned_data.get('message'),
                    'subject': form.cleaned_data.get('subject'),
                    'name': form.cleaned_data.get('name'),
                    'from_email': form.cleaned_data.get('email'),
                    'to': [{
                        'email': 'gabriel@foodfortherestofus.com',
                        'name': 'Gabriel Key',
                    }],
                })
                logging.info('Sent contact email: {0}'.format(form.cleaned_data))
            except mandrill.InvalidKeyError, e:
                logging.error('Cannot send contact email: {0}'.format(
                    form.cleaned_data))
                logging.exception(e)
            except mandrill.Error, e:
                logging.error('Cannot send contact email: {0}'.format(
                    form.cleaned_data))
                logging.exception(e)
            return redirect('contact_complete')
    else:
        form = forms.ContactForm()

    return TemplateResponse(request, 'base/contact.html', {
        'form': form,
    })