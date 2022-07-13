from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UploadFileForm

# Create your views here.


def home(request):
    return render(request, "home.html")


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})
