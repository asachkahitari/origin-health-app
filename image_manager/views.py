from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Image, CustomUser
from .forms import ImageUploadForm, ImageDeleteForm, ImageEditForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required
def dashboard(request):
    images = Image.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(images, 2)

    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    context = {
        'images': images,
    }
    return render(request, 'dashboard.html', context)


@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return redirect('dashboard')
    
    if request.method == 'POST':
        if 'upload_image' in request.POST:
            upload_form = ImageUploadForm(request.POST, request.FILES)
            if upload_form.is_valid():
                image = upload_form.save(commit=False)
                image.user = request.user
                image.save()
                return redirect('admin_dashboard')

        elif 'delete_image' in request.POST:
            delete_form = ImageDeleteForm(request.POST)
            if delete_form.is_valid():
                image_id = delete_form.cleaned_data['image_id']
                Image.objects.filter(id=image_id).delete()
                return redirect('admin_dashboard')
        
        elif 'edit_image' in request.POST:
            edit_form = ImageEditForm(request.POST)
            if edit_form.is_valid():
                image_id = edit_form.cleaned_data['image_id']
                new_label = edit_form.cleaned_data['new_label']
                image = Image.objects.get(id=image_id)
                image.label = new_label
                image.save()
                return redirect('admin_dashboard')

    else:
        upload_form = ImageUploadForm()
        delete_form = ImageDeleteForm()
        edit_form = ImageEditForm()

    
    images = Image.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(images, 2)

    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)

    context = {
        'images': images,
        'upload_form': upload_form,
        'delete_form': delete_form,
        'edit_form': edit_form,
    }
    return render(request, 'admin_dashboard.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            print(user.role)
            if user.role != 'admin':
                return redirect('dashboard')
            return redirect('admin_dashboard')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid login credentials'})
    return render(request, 'registration/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if not CustomUser.objects.filter(username = username).exists():
                user = CustomUser.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'registration/register.html', {'error': 'Username is already taken'})
            
        else:
            return render(request, 'registration/register.html', {'error': 'Passwords do not match'})
        
    return render(request, 'registration/register.html')

