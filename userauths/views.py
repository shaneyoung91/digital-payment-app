from django.shortcuts import render
from userauths.forms import UserRegisterForm

# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()       
    
    context = {
        "form": form
    }
    return render(request, 'userauths/sign-up.html', context)