from django.shortcuts import render
from django.http import HttpResponse

from .forms import AddGroupForm
from users.models import StudentGroup


def index_page(request):
    return HttpResponse("<h3>Главная страница</h3>")

########################  ADMIN  ########################
def add_group(request):
    if request.method == 'POST':
        form = AddGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name='core/admin/group_list.html')
        else:
            return render(request, template_name='core/admin/group_add.html', context={'form': form})
    form = AddGroupForm()
    return render(request, template_name='core/admin/group_add.html', context={'form': form})

def list_groups(request):
    groups = StudentGroup.objects.all()
    return render(request, template_name='core/admin/group_list.html', context={'groups': groups})


