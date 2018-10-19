from django.urls import path

from . import views

app_name = 'tutor'

urlpatterns = [
    # ex: /tutor/
    path('', views.index_view, name = 'index'),

    # ex: /tutor/1/
    path('<int:pk>/', views.each_view, name = 'tutor_detail'),
]
