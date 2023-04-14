from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User

def user_list(request):
    users = User.objects.all()
    return render(request, 'blog/user_list.html', {'users': users})

# Create your views here.
