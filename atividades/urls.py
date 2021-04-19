from django.urls import path

from . import views

urlpatterns = [
    path('', views.atividade_form, name='atividade_insert'),   #get and post req. for insert operation
    path('<int:id>/', views.atividade_form, name='atividade_update'),    #get and post req. for update operation
    path('list/', views.atividade_list, name='atividade_list'),   #get req. to retrieve and display all records.
    path('delete/<int:id>/', views.atividade_delete, name='atividade_delete')
]