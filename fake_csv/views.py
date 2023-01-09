from django.http import HttpResponse


def data_schemas(request):
    return HttpResponse("<h1>data_schemas</h1>")


def new_schema(request):
    return HttpResponse("<h1>new_schema</h1>")
