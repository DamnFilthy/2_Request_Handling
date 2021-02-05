from django.urls import path
from .views import file_list, view_func, file_content, view_file

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам


urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', view_func, name='file_list'),
    path('/content', file_content, name='file_content'),

    path('content/<docnum>', file_content, name='content')
    # path(..., name='file_content'),
]
