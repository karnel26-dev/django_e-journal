from django.shortcuts import render


def teacher_index(request):
    return render(request, template_name='dashboard/teacher/index.html')

def teacher_info(request):
    pass

