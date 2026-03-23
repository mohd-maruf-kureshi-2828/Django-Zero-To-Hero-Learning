from django.http import HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse('Hello This Is BlogHome Page')
