from collections import Counter
from django.http import HttpResponse
from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()

from_original = 0
from_alternate = 0

show_original = 0
show_alternate = 0


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    # click = request.GET['from-landing']
    global from_alternate, from_original
    click = request.GET.get('from-landing', '')
    print(click)
    if click == 'original':
        from_original += 1
    elif click == 'test':
        from_alternate += 1

    print(f'from_original = {from_original}, from_alternate = {from_alternate}')
    return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    global show_alternate, show_original
    arg = request.GET.get("ab-test-arg", "original")

    # output = f'<h1>Argument</h1> = {arg}'
    # return HttpResponse(output)
    if arg == 'original':
        show_original += 1
        print(f'show_original = {show_original}, show_alternate = {show_alternate}')
        return render(request, 'landing.html')
    elif arg == 'alternate':
        show_alternate += 1
        print(f'show_original = {show_original}, show_alternate = {show_alternate}')
        return render(request, 'landing_alternate.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    try:
        test_conversion = (from_alternate / show_alternate) * 100
        original_conversion = (from_original / show_original) * 100
    except ZeroDivisionError:
        test_conversion = 0
        original_conversion = 0
    return render(request, 'stats.html', context={
        'show_original': show_original,
        'show_alternate': show_alternate,
        'from_original': from_original,
        'from_alternate': from_alternate,
        'test_conversion': round(test_conversion),
        'original_conversion': round(original_conversion),
    })
