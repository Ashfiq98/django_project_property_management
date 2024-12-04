from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User  # Import the User model


# View to handle signup (user registration)
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Use your custom form
        if form.is_valid():
            # Check if the username or email already exists
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            # Check for existing username
            if User.objects.filter(username=username).exists():
                messages.error(request, f"The username '{username}' is already taken. Please choose a different username.")
                return render(request, 'signup.html', {'form': form})

            # Check for existing email
            if User.objects.filter(email=email).exists():
                messages.error(request, f"The email '{email}' is already registered. Please use a different email.")
                return render(request, 'signup.html', {'form': form})

            # Save the user if no duplicates
            user = form.save()  # Save the user
            login(request, user)  # Log the user in automatically after registration
            messages.success(request, f"Account has been created as {username}, but {username} needs permission to log in here.")
            return redirect('registration_success')  # Redirect to the success page
    else:
        form = CustomUserCreationForm()  # Use your custom form
    return render(request, 'signup.html', {'form': form})


def registration_success(request):
    return render(request, 'registration_success.html')
