from django.urls import path, re_path
from django.views.generic import DetailView
from django.views.generic import ListView
#from accounts.views import RegisterView

from .views import *
urlpatterns = [

    path('', update_list_view, name='list_view'),
    re_path(r'^(?P<pk>\d)/$', UploadDetailView.as_view(), name='detail_view'),
   # path('', register_page, name='register'),
  #  path('register/', RegisterView.as_view(), name='register'),
]

class UploadListView(ListView):
    queryset = Upload.objects.all()
    template_name = "upload/list_view.html"


class UploadDetailView(DetailView):
    queryset = Upload.objects.all()
    template_name = 'upload/detail_view.html'

   # def get_object(self, queryset=Upload.objects.all()):
    #    print(self.kwargs)
     #   pk = self.kwargs.get("pk")
      #  print(pk)
       # return Tweet.objects.get(id=pk)

