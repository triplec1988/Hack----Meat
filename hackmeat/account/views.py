
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.conf import settings

import mandrill
import logging

import forms


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
