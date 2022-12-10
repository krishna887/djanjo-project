from django.http import HttpResponse

def index(request):
    return HttpResponse("hello,world. You are at the pole index")

# Create your views here.
