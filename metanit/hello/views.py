from email.headerregistry import ContentTypeHeader
from django.shortcuts import HttpResponse

def index(request):
    scheme = request.scheme
    body = request.body
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path

    #return HttpResponse(f"""
    #    <p>Scheme: {scheme}</p>
    #    <p>Body: {body}</p>
    #    <p>Host: {host}</p>
    #    <p>Path: {path}</p>
    #    <p>User-agent: {user_agent}</p>
    #    <p>get_host(): {request.get_host()}</p>
    #    <p>get_port(): {request.get_port()}</p>
    #""")
    #return HttpResponse("Произошла ошибка", status=400, reason="Incorrect Data", headers={"SecretCode": 256})
    return HttpResponse("<h1>Hello</h1>", content_type="text/plain", charset="utf-8")

def about(request, name, age):
    return HttpResponse(f"""
    <h2>О сайте</h2>
    <p>Имя: {name}</p>
    <p>Возраст: {age}</p>
    """)

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
