from django.urls import path

from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.usuario_form, name='usuario_insert'),    #get and post req. for insert operation
    path('<int:id>/', views.usuario_form, name='usuario_update'),    #get and post req. for update operation
    path('list/', views.usuario_list, name='usuario_list'),   #get req. to retrieve and display all records.
    path('delete/<int:id>/', views.usuario_delete, name='usuario_delete'),
    path('login/', views.login, name='login'),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

]