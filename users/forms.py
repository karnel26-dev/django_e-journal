from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import StudentProfile, ParentProfile, TeacherProfile


User = get_user_model()

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Электронная почта",
        # help_text="Введите действующий email, на него придет ссылка для активации.",
        error_messages={
            'required': "Обязательное поле!",
            'invalid': "Некорректный email.",
        }
    )
    role = forms.ChoiceField(
        label="Роль",
        choices=User.ROLES,
        widget=forms.Select(attrs={'id': 'id_role'}),
        # help_text="Выберите вашу роль в системе.",
        error_messages={
            'required': "Укажите роль!",
        }
    )

    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput,
        # help_text=UserCreationForm.base_fields['password1'].help_text,
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        strip=False,
        widget=forms.PasswordInput,
        # help_text=UserCreationForm.base_fields['password2'].help_text,
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'role', 'birth_date', 'photo')
        labels = {
            'username': 'Логин',
            'birth_date': 'Дата рождения',
            'photo': 'Фото'
        }
        help_texts = {
            'username': ''
        }

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['faculty', 'group']
        labels = {
            'faculty': 'Факультет',
            'group': 'Группа'
        }

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['faculty', 'position']
        labels = {
            'faculty': 'Факультет',
            'position': 'Должность'
        }

class ParentProfileForm(forms.ModelForm):
    class Meta:
        model = ParentProfile
        fields = ['phone', 'child']
        labels = {
            'phone': 'Телефон',
            'child': 'Студент'
        }