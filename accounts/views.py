'''
from django.shortcuts import render

from django.views.generic import CreateView

from accounts.forms import RegisterForm

def contact_page(request):
    return render(request, "contact/contact.html")
# Create your views here.
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = '/'
    return render(request, 'auth/register.html',)
'''