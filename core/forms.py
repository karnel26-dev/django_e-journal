from django import forms
from users.models import StudentGroup


class AddGroupForm(forms.ModelForm):
    class Meta:
        model = StudentGroup
        fields = ('number',)
