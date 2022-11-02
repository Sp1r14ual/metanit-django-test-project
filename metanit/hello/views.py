from django.http import HttpResponse

def index(request):
    return HttpResponse("Главная страница")

def user(request):
    name = request.GET.get("name", "Undefined")
    age = request.GET.get("age", 0)
    return HttpResponse(f"<h2>Имя: {name}, Возраст: {age}</h2>")

