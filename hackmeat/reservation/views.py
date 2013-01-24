from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.conf import settings

import mandrill
import logging

from hackmeat.reservation.forms import *


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
        reservation_form = ReservationForm(request.POST, prefix = "reservation")
        if reservation_form.is_valid():
            reservation_form.save()
            
            return redirect('cut_form')
    else:
        reservation_form = ReservationForm(prefix = "reservation")
        
    return TemplateResponse(request, 'reservation/reservation.html', {
            'reservation_form': reservation_form,
    })


def cut_step(request):
    if request.method == 'POST':
        cut_form = Cut_FormForm(request.POST, prefix = "cut")
        if cut_form.is_valid():
            cut_form.save()
            
            return redirect('res_complete')
    else:
        cut_form = Cut_FormForm(prefix = "cut")
        
    return TemplateResponse(request, 'reservation/cut_step.html', {
            'cut_form': cut_form,
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