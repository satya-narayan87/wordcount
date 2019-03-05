from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1>This is my first program in django</h1>")

def contact_us(request):
    return HttpResponse("<h1>contact page</h1><br>This is our contact page")