import datetime
import os
from django.conf import settings
from django.http import HttpResponse

from django.shortcuts import render


def view_func(request):
    directory = 'C:\\Program Files\\netology_homework_all_courses\\Python_prof34_course\\z_django_block\\2_Request_Handling\\file_server\\files'
    files = os.listdir(directory)
    return render(request, 'index.html', {'files': files,
                                          'ctime': datetime.datetime(2018, 1, 1),
                                          'mtime': datetime.datetime(2018, 1, 2)
                                          })


def file_list(request):
    template_name = 'index.html'

    directory = 'file_server/files'
    files = os.listdir(directory)

    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    # context = {
    #     'files': [
    #         {'name': 'file_name_1.txt',
    #          'ctime': datetime.datetime(2018, 1, 1),
    #          'mtime': datetime.datetime(2018, 1, 2)}
    #     ],
    #     'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
    # }
    context = {'files': files}

    return render(request, template_name, context)


def file_content(request, docnum):
    print(docnum)
    file = open(
        f'C:\\Program Files\\netology_homework_all_courses\\Python_prof34_course\\z_django_block\\2_Request_Handling\\file_server\\files\\{docnum}')
    template_name = 'file_content.html'
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    return render(
        request, template_name, {'file_name': docnum,
                                 'file_content': file}
    )
    # return HttpResponse(f'Hello from file {docnum}')


def view_file(request):
    return HttpResponse(f'Hello from file!')
