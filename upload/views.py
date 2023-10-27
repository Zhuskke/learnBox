from django.http import HttpResponse
from django.shortcuts import render
from .forms import TaskSubmissionForm

def upload_file(request):
    form = None
    if request.method == 'POST':
        form = TaskSubmissionForm(request.FILES, request.POST)
        print(form)
        if form.is_valid():
            # file is saved
            form.save()
            print('Form is valid')
            return HttpResponse('thanks')
        print('Form is not valid')
    else:
        form = TaskSubmissionForm()
    return render(request, 'upload/upload_file.html', {'form': form})