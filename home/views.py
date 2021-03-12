from django.shortcuts import render
from checkout.views import check_active_plan
# Create your views here.


def index(request):
    """ A view to return the index page """
    check_active_plan()
    return render(request, 'home/index.html')
