from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login


# View to handle signup (user registration)
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log the user in automatically after registration
            messages.success(request, 'Your account has been created and you are logged in!')
            return redirect('signup')  # Redirect to the home page or another page you want
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
