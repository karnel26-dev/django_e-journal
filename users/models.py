from django.contrib.auth.models import AbstractUser
from django.db import models


FACULTIES = (
        ('sociology', 'Факультет социологии'),
        ('mathematical_sciences', 'Факультет математических наук'),
        ('information_technology', 'Факультет иноформационных технологий'),
)

POSITIONS = (
        ('assistant', 'Ассистент'),
        ('teacher', 'Преподаватель'),
        ('senior_lecturer', 'Старший преподаватель'),
        ('associate_professor', 'Доцент'),
        ('professor', 'Профессор'),
)

GROUPS = (
        ('1132', '1132'),
        ('1133', '1133'),
        ('1245', '1245'),
        ('1246', '1246'),
        ('2346', '2346'),
)

class User(AbstractUser):
    ROLES = (
        ('student', 'Студент'),
        ('teacher', 'Преподаватель'),
        ('parent', 'Родитель'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='student')
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    faculty = models.CharField(max_length=100, choices=FACULTIES)
    group = models.CharField(max_length=10, choices=GROUPS)

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    faculty = models.CharField(max_length=100, choices=FACULTIES)
    position = models.CharField(max_length=100, choices=POSITIONS)

class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent_profile')
    child = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='parents')
    phone = models.CharField(max_length=20)