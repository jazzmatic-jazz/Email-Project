from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .form import ContactForm
from django.urls import reverse_lazy

# Create your views here.

class ContactView(FormView):
    template_name = 'send/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('send:success')

    def form_valid(self, form):
        #calls the custom send method
        form.send()
        return super().form_valid(form)
    

class ContactSuccessView(TemplateView):
    template_name = 'send/success.html'