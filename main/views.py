from django.shortcuts import render


def index(request):
    student_list = Student.objects.all()
    context = {
        'object_list': student_list
    }
    return render(request, 'main/index.html')

# def index(request):
#     if request.method == 'POST':
#         """Метод для приема инфы с фронтэнда и ее вывода в консоль"""
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} ({email}): {message}')
#     return render(request, 'main/index.html')
