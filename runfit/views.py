from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from runfit.forms import UserForm, UserFormForEdit, PersonForm, OrderForm
from runfit.models import Order


def home(request):
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def service(request):
    return render(request, 'services.html')


def not_found(request):
    return render(request, '404.html')


def sign_up(request):
    user_form = UserForm()
    person_form = PersonForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)
        person_form = PersonForm(request.POST, request.FILES)

        if user_form.is_valid() and person_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_person = person_form.save(commit=False)
            new_person.user = new_user
            new_person.save()

            login(request, authenticate(
                username=user_form.cleaned_data["username"],
                password=user_form.cleaned_data["password"]
            ))
            return redirect(home)

    return render(request, 'sign_up.html', {
        "user_form": user_form,
        "person_form": person_form
    })


@login_required(login_url='/sign-in/')
def order(request):
    order_form = OrderForm
    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            new_order = order_form.save(commit=False)
            new_order.save()
            return redirect(home)

    return render(request, 'order.html', {
        "order_form": order_form,
    })
