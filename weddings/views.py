# weddings/views.py
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import WeddingImage, Folder
from django.shortcuts import get_object_or_404, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def home(request):
    folders = Folder.objects.all()
    return render(request, 'home.html')
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, email=email, password=password)
            login(request, user)
            return redirect('folder_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('folder_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def folder_list(request):
    folders = Folder.objects.all()
    return render(request, 'folder_list.html', {'folders': folders})

def image_list(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    images = WeddingImage.objects.filter(folder=folder)
    return render(request, 'image_list.html', {'folder': folder, 'images': images})

def image_detail(request, image_id):
    image = get_object_or_404(WeddingImage, pk=image_id)
    return render(request, 'image_detail.html', {'image': image})

@login_required
def download_image(request, image_id):
    image = get_object_or_404(WeddingImage, pk=image_id)
    # Create an HTTP response with the image file for download
    response = HttpResponse(image.image, content_type='image/jpeg')
    response['Content-Disposition'] = f'attachment; filename="{image.title}.jpg"'
    return response




