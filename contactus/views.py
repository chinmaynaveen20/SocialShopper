from django.shortcuts import render

# Create your views here.
def contact(request):
    loggedIn = request.user.is_authenticated
    context = {"loggedIn" : loggedIn}
    return render(request, "contact.html", context)
