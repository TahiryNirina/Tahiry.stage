from django.shortcuts import render, redirect
from .forms import FileForm
from .models import File
from django.views.generic import View


def index(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return redirect('file')
    else:
        form = FileForm()
        files = File.objects.all()
    return render(request, 'index.html', {'form': form, 'files':files})
    

def deletefile(request_id):
    file = File.objects.get(id=request_id)
    file.delete()
    return redirect('index')    


