from django.http import HttpResponse
from django.shortcuts import render, reverse

from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now().strftime('%H:%M:%S')
    time = f'Текущее время: {current_time}'
    print(time)
    return HttpResponse(time)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    files = os.listdir(os.getcwd())
    files_html = "<ul>"
    for file in files:
        files_html += "<li>{}</li>".format(file)
    files_html += "</ul>"
    workdir = 'Содержимое рабочей директории: {}'.format(str(files_html))
    print(workdir)
    return HttpResponse(workdir)

    raise NotImplemented
