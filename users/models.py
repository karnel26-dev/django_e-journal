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
        ('professor', 'Профессор')
)

class StudentGroup(models.Model):
    number = models.CharField(max_length=4)
    teachers = models.ManyToManyField('User', related_name='st_groups')


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
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    faculty = models.CharField(max_length=100, choices=FACULTIES)
    position = models.CharField(max_length=100, choices=POSITIONS)

class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent_profile')
    child = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='parents')
    phone = models.CharField(max_length=20)