from django.shortcuts import render, redirect
from .forms import (BaseRegisterForm, StudentProfileForm,
                    TeacherProfileForm, ParentProfileForm)


def register(request):
    if request.method == 'POST':
        user_form = BaseRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            role = user.role

            # Определяем форму профиля в зависимости от роли
            if role == 'student':
                profile_form = StudentProfileForm(request.POST)
            elif role == 'teacher':
                profile_form = TeacherProfileForm(request.POST)
            elif role == 'parent':
                profile_form = ParentProfileForm(request.POST)

            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('login')
            else:
                # Если форма профиля невалидна, передаем её в контекст
                return render(request, 'users/register.html', {
                    'user_form': user_form,
                    'profile_form': profile_form,
                })
        # Если форма пользователя невалидна, передаем только её
        return render(request, 'users/register.html', {
            'user_form': user_form,
        })
    else:
        # GET-запрос: передаем все формы в контекст
        user_form = BaseRegisterForm()
        return render(request, 'users/register.html', {
            'user_form': user_form,
        })
