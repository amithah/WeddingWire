import json
from django.shortcuts import render, redirect, reverse
from .models import Page, Image
from .forms import ImageAddForm, ContentEditForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage


def load_design_1(request, action):
    page = Page.objects.get(user=request.user)
    return render(request, 'page/index_edit.html', {'action': action, 'page': page})


def load_webpage(request,slug):
    page = Page.objects.get(user=request.user)
    return render(request, 'page/index_edit.html', {'slug': page.slug, 'page': page})


@csrf_exempt
def edit_content(request):
    page = Page.objects.get(user=request.user)
    if request.method == 'POST':
        form = ContentEditForm(request.POST)
        if form.is_valid():
            page.groom_name = form.cleaned_data['groom_name']
            page.bride_name = form.cleaned_data['bride_name']
            page.city = form.cleaned_data['city']
            page.date = form.cleaned_data['date']
            page.save()
            return JsonResponse({'status': "success"})
            # return redirect(reverse('design1', args=['edit']))
    else:
        form = ContentEditForm()
    return render(request, 'page/form.html', {'form': form})


@csrf_exempt
def add_image(request):
    user = request.user
    page = Page.objects.get(user=user)
    image, create = Image.objects.get_or_create(page=page)
    if request.method == 'POST':
        if request.POST['image_type'] == "bride_img":
            image.bride_image = request.POST['uploaded_path']
        elif request.POST['image_type'] == "groom_img":
            image.groom_image = request.POST['uploaded_path']
        else:
            return JsonResponse({"status": "failed"})
        image.save()
        return JsonResponse({"status": "success"})


@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES['file']:
        image = request.FILES['file']
        fs = FileSystemStorage()
        image_name = fs.save(image.name, image)
        uploaded_image_url = fs.url(image_name)
    else:
        print("oops! this is a GET")

    return JsonResponse({'uploaded_path': uploaded_image_url})

