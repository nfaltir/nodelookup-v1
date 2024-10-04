from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegistrationForm 
from django.contrib.auth import login,logout, authenticate

# REGISTER
def register_view(request):
    page_title = "Register"
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Create the user manually
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            
            # Log the user in immediately after registration
            login(request, user)
            return redirect("home")
    else:
        form = RegistrationForm()  # Use this form for GET requests

    context = {
        "page_tile": page_title,
        "form": form,
    }
    return render(request, "register.html", context)


#LOGIN
def login_view(request):
    page_title = "Login"
    
    if request.method == "POST":
        form = LoginForm(data=request.POST)  # Only pass data=request.POST, not request itself
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to the home page after login
            else:
                form.add_error(None, "Invalid username or password")  # Add a non-field error
    else:
        form = LoginForm()

    context = {
        "page_title": page_title,
        "form": form,
    }
    return render(request, "login.html", context)

#LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')