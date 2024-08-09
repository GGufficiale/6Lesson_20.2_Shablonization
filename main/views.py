from django.shortcuts import render
from main.models import Student


def index(request):
    student_list = Student.objects.all()
    context = {
        'object_list': student_list,
        'title': 'Главная'
    }
    return render(request, 'main/index.html', context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        """Метод для приема инфы с фронтэнда и ее вывода в консоль"""
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    return render(request, 'main/contact.html', context)
