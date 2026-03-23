from django.http import HttpResponse

def blogPrice(request,id):
    return HttpResponse(f'the price is : {id} ')

def details(request,**kwargs):
    # return HttpResponse(f'Details Is : {kwargs}')
    return HttpResponse(f'Details Is : {kwargs["name"]} And Age Is : {kwargs["age"]}')
