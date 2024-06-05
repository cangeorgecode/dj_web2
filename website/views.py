from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages


def index(request):
    websites = Website.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Enquiry"
            body = {
                'name': form.cleaned_data['Name'],
                'subject': form.cleaned_data['Subject'],
                'email': form.cleaned_data['Email'],
                'message': form.cleaned_data['Message']
            }
            message = f"""
            Received message below message: {body}
            """
            try:
                send_mail(subject, message, 'bobbyesaev@gmail.com', ['crayfishconfessionists@gmail.com'])
                messages.success(request, 'Your message has been sent')
            except:
                return HttpResponse('Invalid header')

            return redirect('/')
    return render(request, 'website/index.html', {'websites': websites, 'form': form})

def portfolio(request, id):
    website = Website.objects.get(id=id)
    return render(request, 'website/portfolio.html', {'website': website})
