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
            full_name = request.POST.get('full_name', '')
            email_address = request.POST.get('email_address', '')
            message = request.POST.get('message', '')

            # Email the profile with the
            # contact information
            template = get_template('enquiries/enquiries_template.txt')
            context = {
                'full_name': full_name,
                'email_address': email_address,
                'message': message,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremail@gmail.com'], headers={'Reply-To': email_address}
            )
            email.send()
            return redirect('enquiries')

    return render(request, 'enquiries/enquiries.html', {
        'form': form_class,
    })
