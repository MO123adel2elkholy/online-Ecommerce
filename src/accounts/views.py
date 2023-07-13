from django.shortcuts import render, redirect, get_list_or_404
from  django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Profile
from django.contrib.auth import login , authenticate
from .forms import userform, profileform
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('data saved')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user= authenticate(username=username, password=password)
            login(request,user)
            redirect('/')
        print('posted')
    else :
        form = UserCreationForm()
    c = {'form': form}
    return render(request, 'registration/signup.html',context= c)

@login_required(redirect_field_name="my_redirect_field")
def my_profile(request, slug):
    data = Profile.objects.get(slug=slug)
    co={"profile":data}
    return render(request, 'registration/profile.html', context=co)
