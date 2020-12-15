from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import get_template


# Create your views here.


def enquiries(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            full_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('enquiries/enquiries_template.txt')
            context = {
                'full_name': full_name,
                'contact_email': contact_email,
                'content': content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremail@gmail.com'], headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('enquiries')

    return render(request, 'enquiries/enquiries.html', {
        'form': form_class,
    })
