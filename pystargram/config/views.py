from django.shortcuts import render, redirect


def index(request):
    if not request.user.is_authenticated:
        return redirect("/posts/feeds/")

    return redirect("/users/login/")
    # return render(request, "index.html")
