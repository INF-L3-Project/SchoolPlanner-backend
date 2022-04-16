from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from authentication.forms import InstitutionSignUpForm
from authentication.models import Institution
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "registration/home.html", context={})


class InstitutionRegisterView(View):
    form_class = InstitutionSignUpForm
    template_name = 'registration/register.html'


    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, context={"form":form})
    

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            firstN = request.POST['first_name']
            lastN = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password1']
            user = User.objects.create_user(username=username, email=email, password=password, first_name=firstN, last_name=lastN)
            user.save()
            instName = request.POST['institution_name']
            instLogo = request.POST['institution_logo']
            instDesc = request.POST['institution_description']
            Institution.objects.create(user=user, name=instName, logo=instLogo, description=instDesc)
            login(request, user)
            return redirect("home")
        else:
            return render(request, self.template_name, context={"form":form})


def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "registration/login.html", context={"message":"User don't exist !"})
    else:
        return render(request, "registration/login.html", context={})


def logoutUser(request):
    logout(request)
    return redirect("home")



