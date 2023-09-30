from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib import admin
from .models import Upload
from .forms import UploadModelForm

class UploadModelAdmin(admin.ModelAdmin):
    form = UploadModelForm

admin.site.register(Upload, UploadModelAdmin)