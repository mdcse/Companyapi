from django.http import HttpResponse, JsonResponse

def homePage(request):
    friends = ['John', 'Paul', 'George', 'Ringo']
    return JsonResponse(friends, safe=False)