from django.shortcuts import render

# Create your views here.


def view_enquiries(request):
    """ A view that renders the bag contents page """

    return render(request, 'enquiries/enquiries.html')
