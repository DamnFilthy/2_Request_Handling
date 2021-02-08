from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings

import csv

from numpy.core import number

res_dict = {}
res_list = []
csvfile = open(settings.BUS_STATION_CSV, encoding='cp1251')
reader = csv.DictReader(csvfile)
for row in reader:
    res_dict['Name'] = row['Name']
    res_dict['Street'] = row['Street']
    res_dict['District'] = row['District']
    res_list.append(res_dict.copy())


# print(res_list)


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(res_list, settings.REQS_POSTS_PER_PAGE)
    page = paginator.get_page(page_number)

    msg = page.object_list

    current_page = page.number
    all_pages = paginator.num_pages

    try:
        prev_page_url = page.previous_page_number
    except EmptyPage:
        prev_page_url = None
    next_page_url = page.next_page_number

    return render(request, 'index.html', context={
        'bus_stations': msg,
        'page': page,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
        'all_pages': all_pages
    })
