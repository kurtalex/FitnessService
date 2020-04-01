from django.shortcuts import render, redirect


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
