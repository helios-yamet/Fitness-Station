from django.shortcuts import render
from collection.forms import ContactForm


# Create your views here.


def contact(request):
    form_class = ContactForm

    return render(request, 'enquiries/enquiries.html', {
        'form': form_class,
    })
