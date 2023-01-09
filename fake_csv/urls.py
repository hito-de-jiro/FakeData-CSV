from django.urls import path

from . import views

urlpatterns = [
    path('dataschemas/', views.data_schemas),
    path('newschema/', views.new_schema),
]
