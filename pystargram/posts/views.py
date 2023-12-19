from django.shortcuts import render, redirect


# Create your views here.
def feeds(request):
    user = request.user
    is_authenticated = user.is_authenticated
    print(f"User: {user}")
    print(f"Is Authenticated: {is_authenticated}")

    if is_authenticated is False:
        return redirect("/users/login/")

    return render(request, "posts/feeds.html")
