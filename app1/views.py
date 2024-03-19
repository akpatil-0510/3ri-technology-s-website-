from django.shortcuts import render,HttpResponse, redirect
from .forms import Signupform
from django.contrib.auth.forms import AuthenticationForm   # for signin view
from django.contrib.auth import authenticate, login, logout # for sign in
from .forms import FeedbackForm
from .models import Feedback
from app1.models import Contact
from django.contrib import messages


# Create your views here.
def home(reuqest):
    return render(reuqest,'home.html')


def signup(request):
    if request.method == "POST":
        fm = Signupform(request.POST)
        if fm.is_valid():
            fm.save()
            # messages.success(request, 'You have register successfully.')
            return redirect("signin")
    else:    
        fm=Signupform()
    return render(request,'Signup.html',{'fm':fm})
   
def signin(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return render(request, 'home.html', {'user': user,})
    else:
        fm = AuthenticationForm()
    return render(request, "signin.html", {'user_data': fm})

def signout(request):
    logout(request)
    return redirect('/')

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def feedback_success(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'feedback_success.html', {'feedbacks': feedbacks})

from .models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        # phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact_instance = Contact(name=name, email=email, desc=desc)
        contact_instance.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

 




