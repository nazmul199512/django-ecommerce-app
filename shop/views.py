from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *

from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def shop(request):
    query_set = Product.objects.all()
    paginator = Paginator(query_set, 12)  # Show 12 product per page
    page = request.GET.get('page')
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        query_set = paginator.page(1)
    except EmptyPage:
        query_set = paginator.page(paginator.num_pages)

    context = {
        'products': query_set
    }
    return render(request, 'shop/shop.html', context)


def shop_details_1(request):
    query_set = Product.objects.all()

    paginator = Paginator(query_set, 12)  # Show 12 product per page
    page = request.GET.get('page')
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        query_set = paginator.page(1)
    except EmptyPage:
        query_set = paginator.page(paginator.num_pages)

    context = {
        'product_details_1': query_set
    }
    return render(request, 'shop/shop_details_1.html', context)


def shop_details_2(request):
    query_set = Product.objects.all()
    paginator = Paginator(query_set, 12)  # Show 12 product per page
    page = request.GET.get('page')
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        query_set = paginator.page(1)
    except EmptyPage:
        query_set = paginator.page(paginator.num_pages)

    context = {
        'product_details_2': query_set
    }
    return render(request, 'shop/shop_details_2.html', context)


def shop_details_3(request):
    query_set = Product.objects.all()
    paginator = Paginator(query_set, 12)  # Show 12 product per page
    page = request.GET.get('page')
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        query_set = paginator.page(1)
    except EmptyPage:
        query_set = paginator.page(paginator.num_pages)

    context = {
        'product_details_3': query_set
    }
    return render(request, 'shop/shop_details_3.html', context)


def shop_details_4(request):
    query_set = Product.objects.all()
    paginator = Paginator(query_set, 12)  # Show 12 product per page
    page = request.GET.get('page')
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        query_set = paginator.page(1)
    except EmptyPage:
        query_set = paginator.page(paginator.num_pages)

    context = {
        'product_details_4': query_set
    }
    return render(request, 'shop/shop_details_4.html', context)

