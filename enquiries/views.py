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
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('enquiries_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
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
