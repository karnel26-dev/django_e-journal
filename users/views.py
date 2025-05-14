from django.shortcuts import render, redirect
from .forms import (BaseRegisterForm, StudentProfileForm,
                    TeacherProfileForm, ParentProfileForm)


# def register(request):
#     if request.method == 'POST':
#         user_form = BaseRegisterForm(request.POST)
#         if user_form.is_valid():
#             user = user_form.save()
#             role = user.role
#
#             # Определяем форму профиля в зависимости от роли
#             if role == 'student':
#                 profile_form = StudentProfileForm(request.POST)
#             elif role == 'teacher':
#                 profile_form = TeacherProfileForm(request.POST)
#             elif role == 'parent':
#                 profile_form = ParentProfileForm(request.POST)
#
#             if profile_form.is_valid():
#                 profile = profile_form.save(commit=False)
#                 profile.user = user
#                 profile.save()
#                 return redirect('index')
#             else:
#                 # Если форма профиля невалидна, передаем её в контекст
#                 return render(request, 'users/register.html', {
#                     'user_form': user_form,
#                     'profile_form': profile_form,
#                 })
#         # Если форма пользователя невалидна, передаем только её
#         return render(request, 'users/register.html', {
#             'user_form': user_form,
#
#         })
#     else:
#         # GET-запрос: передаем все формы в контекст
#         user_form = BaseRegisterForm()
#         student_form = StudentProfileForm()
#         teacher_form = TeacherProfileForm()
#         parent_form = ParentProfileForm()
#         return render(request, 'users/register.html', {
#             'user_form': user_form,
#             'student_form': student_form,
#             'teacher_form': teacher_form,
#             'parent_form': parent_form
#         })
def register(request):
    if request.method == 'POST':
        user_form = BaseRegisterForm(request.POST)
        role = request.POST.get('role')

        if user_form.is_valid():
            user = user_form.save()

            if role == 'student':
                profile_form = StudentProfileForm(request.POST)
            elif role == 'teacher':
                profile_form = TeacherProfileForm(request.POST)
            elif role == 'parent':
                profile_form = ParentProfileForm(request.POST)
            else:
                # Обработка неверной роли
                pass

            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('index')
    else:
        user_form = BaseRegisterForm()

    return render(request, 'users/register.html', {'user_form': user_form})


def get_profile_form(request):
    role = request.GET.get('role')

    if role == 'student':
        form = StudentProfileForm()
    elif role == 'teacher':
        form = TeacherProfileForm()
    elif role == 'parent':
        form = ParentProfileForm()
    else:
        form = None

    return render(request, 'users/profile_form_partial.html', {'form': form})