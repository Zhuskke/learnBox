from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, ListView
from .models import Upload
User = get_user_model()

def register_page(request):
   form = RegisterForm(request.POST or None)
   context = {
       'form':form
   }

   if form.is_valid():
       username = form.cleaned_data.get("username")
       email = form.cleaned_data.get("email")
       password = form.cleaned_data.get("password")
       newUser = User.object.create_user(username, email, password)

   return render(request, "auth/register.html", context)


# Create your views here.
def update_detail_view(request, pk=None):
    obj = get_object_or_404(Upload, pk=pk)
    print(obj)
    context = {
        'object': obj,
    }
    return render(request, 'upload/detail_view.html', context)


def update_list_view(request):
    qs = Upload.objects.all()
    print(qs)
    context = {
        'query': qs,
    }
    return render(request, 'list_view.html', context)


class UploadDetailView(DetailView):
    queryset = Upload.objects.all()
    template_name = 'detail_view.html'


# def get_object(self, queryset=Upload.objects.all()):
#    print(self.kwargs)
#   pk = self.kwargs.get("pk")
#  print(pk)
# return Tweet.objects.get(id=pk)

class UploadListView(ListView):
    queryset = Upload.objects.all()
    template_name = "upload/list_view.html"
