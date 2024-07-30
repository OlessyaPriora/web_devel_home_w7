from django.http import HttpResponse


def greet(request, name):
    return HttpResponse(f"<h1>Hello, {name}!</h1>")


