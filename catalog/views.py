from django.shortcuts import render, redirect, reverse
from .forms import CreateWebsiteForm
from accounts.models import CustomUser
from django.contrib.auth import login
from page.models import Page,Image
import random
import string


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def home(request):
    return render(request, 'catalog/home.html', {})


def create_website(request):
    # validate form and create a new user
    # create a page object  and connect user id  to that page object
    # check the design opted by user
    # redirect user to the opted design html , with edit=True

    if request.method == 'POST':
        form = CreateWebsiteForm(request.POST)
        if form.is_valid():
            if not CustomUser.objects.filter(email=form.cleaned_data['email']).exists():
                user = CustomUser.objects.create(username=get_random_string(6), email=form.cleaned_data['email'])
                login(request, user)
                page = Page.objects.create(
                    user=user,
                    email=form.cleaned_data['email'],
                    groom_name=form.cleaned_data['groom_name'],
                    bride_name=form.cleaned_data['bride_name'],
                    design=form.cleaned_data['design'],
                    city=form.cleaned_data['city'],
                    date=form.cleaned_data['date'],
                    slug=get_random_string(4),
                )

                return redirect(reverse('design1', args=['edit']))
            else:
                # redirect user to previously created website
                return redirect(reverse('design1', args=['edit']))
    else:
        if request.user.is_anonymous:
            form = CreateWebsiteForm()
            return render(request, 'catalog/page_creation_form.html', {'form': form})
        else:
            return redirect(reverse('design1', args=['edit']))
