from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden
 
def index(request, id):
    people = ["Tom", "Bob", "Sam"]
    if id in range(0, len(people)):
        return HttpResponse(people[id])
    else:
        return HttpResponseNotFound("Not Found")
 
def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    if(age > 17):
        return HttpResponse("Доступ разрешен")
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")