from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# our apps
from ourteam.models import Ourteam
from digitalmarketingservices.models import digitalservices
from graphicdesignservices.models import graphicservices
from techsolutionservices.models import techservices
from contactform.models import contactForm
from newsletter.models import Newsletter


def home(request):
    ourteamData = Ourteam.objects.all()
    data = {
        "ourteamData": ourteamData,
    }
    return render(request, "index.html", data)


def about(request):
    ourteamData = Ourteam.objects.all()
    data = {
        "ourteamData": ourteamData,
    }
    return render(request, "about.html", data)


def services(request):
    ourteamData = Ourteam.objects.all()
    data = {
        "ourteamData": ourteamData,
    }
    return render(request, "services.html", data)


def contact(request):
    return render(request, "contact.html")


def digitalmarketing(request):
    digitalmarketingservicesData = digitalservices.objects.all()
    ourteamData = Ourteam.objects.all()
    data = {
        "ourteamData": ourteamData,
        "digitalmarketingservicesData": digitalmarketingservicesData,
    }
    return render(request, "digital marketing.html", data)


def graphicdesign(request):
    graphicdesignservicesData = graphicservices.objects.all()
    ourteamData = Ourteam.objects.all()
    data = {
        "ourteamData": ourteamData,
        "graphicdesignservicesData": graphicdesignservicesData,
    }
    return render(request, "graphicdesign.html", data)


def ITsolution(request):
    techsolutionservicesData = techservices.objects.all()
    ourteamData = Ourteam.objects.all()
    data = {
        "ourteamData": ourteamData,
        "techsolutionservicesData": techsolutionservicesData,
    }
    return render(request, "ITsolution.html", data)


def travelagency(request):
    ourteamData = Ourteam.objects.all()
    data = {
        "ourteamData": ourteamData,
    }
    return render(request, "travel agency.html", data)


def signup(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if pass1 != pass2:
            return HttpResponse("your password and  confirm password are not same")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect("login")

    return render(request, "signup.html")


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)

            return redirect("home")
        else:
            return HttpResponse("incorrect username or password please try again")

    return render(request, "login.html")


def logoutPage(request):
    if request.method == "GET":
        logout(request)
        return redirect("home")
    return HttpResponse("logout")


def saveenquiry(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        data = contactForm(name=name, email=email, subject=subject, message=message)
        data.save()
    return render(request, "index.html")


def saveenquiry2(request):
    if request.method == "POST":
        email = request.POST.get("email")

        data = Newsletter(email=email)
        data.save()
    return render(request, "index.html")
