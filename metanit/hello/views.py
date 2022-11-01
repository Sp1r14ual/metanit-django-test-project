from django.shortcuts import HttpResponse

def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path

    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
    """)

def about(request, name, age):
    return HttpResponse(f"""
    <h2>О сайте</h2>
    <p>Имя: {name}</p>
    <p>Возраст: {age}</p>
    """)

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
