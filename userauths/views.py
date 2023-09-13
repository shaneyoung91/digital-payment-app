from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            new_user = form.save() # new_user.email
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey {username}, your account was created successfully.")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("main_app:index")
    
    elif request.user.is_authenticated:
        messages.warning(request, f"You are already logged in.")
        return redirect("main_app:index")
    
    else:
        form = UserRegisterForm()       
    
    context = {
        "form": form
    }
    return render(request, 'userauths/sign-up.html', context)