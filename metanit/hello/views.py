from django.http import JsonResponse

def index(request):
    return JsonResponse({"Name": "Tom", "Age": 38})