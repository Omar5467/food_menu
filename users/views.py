from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import RegisterForm
app_name = 'users'
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'wellcome {username}, your account has been created successfully')
            return redirect('myapp:index')
    form = RegisterForm()
    return render(request,'users/register.html', {'form': form})
    # return HttpResponse('Hello, World!')