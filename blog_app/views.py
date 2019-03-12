from django.shortcuts import render, redirect
from django.contrib import messages
from blog_app.models import Menu, HomePage, Article, Footer
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from blog_app.forms import RegisterForm
from django.urls import reverse


def common_data():
    return {
    "menu_list":Menu.objects.filter(status=True),
    "footer":Footer.objects.last(),
}

def index(request):
    context = common_data()
    context["header"] = HomePage.objects.last()
    context["content_list"] = Article.objects.all()[:5]
    return render(request, 'home.html', context)

def detail_content(request, pk):
    context = common_data()
    context["content"] = Article.objects.get(pk=pk)
    return render(request, "detail.html", context)

def login_view(request):
    if not request.user.is_authenticated:
        context = common_data()
        context["form"] = AuthenticationForm()
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return render(request, "login.html", context)
            else:
                return render(request, "login.html", context)
        else:
            return render(request, "login.html", context)
    else:
        return redirect("/")

def logout_view(request):
    logout(request)
    return redirect("/")

def register_view(request):
    if not request.user.is_authenticated:
        context = {}
        context["form"] = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST)
            context["form"] = form
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(request.POST.get("password2"))
                user.username = request.POST.get("username")
                try:
                    user.save()
                except:
                    context["error"] = "The {} have in database!".format(request.POST.get("username"))
                    return render(request, "register.html", context)
                messages.info(request, "Congratulation you are logined!")
                return redirect(reverse("login-view"))
            else:
                return render(request,"register.html", context)
        else:
            return render(request, "register.html", context)
    else:
        return redirect("/")