from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import StudentProfile, ParentProfile, TeacherProfile


User = get_user_model()

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Электронная почта",
        help_text="Введите действующий email, на него придет ссылка для активации.",
        error_messages={
            'required': "Обязательное поле!",
            'invalid': "Некорректный email.",
        }
    )
    role = forms.ChoiceField(
        label="Роль",
        choices=User.ROLES,
        help_text="Выберите вашу роль в системе.",
        error_messages={
            'required': "Укажите роль!",
        }
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role', 'birth_date', 'photo')
        labels = {
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Повторите пароль',
            'role': 'Роль',
            'birth_date': 'Дата рождения',
            'photo': 'Фото'
        }

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['faculty', 'group']

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['faculty', 'position']

class ParentProfileForm(forms.ModelForm):
    class Meta:
        model = ParentProfile
        fields = ['phone', 'child']