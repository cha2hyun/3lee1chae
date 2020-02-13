from django.shortcuts import render
from .forms import RegisterForm
from django.shortcuts import redirect
# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()

            return redirect('/')
        else:
            return redirect('/register')
    else:
        user_form = RegisterForm()

        return render(request, 'registration/register.html', {'form': user_form})
