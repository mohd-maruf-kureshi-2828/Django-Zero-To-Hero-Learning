from django.urls import path
from .import views

urlpatterns = [
    # path('blog/<int:id>/',views.blogPrice,name='blogPrice')
    path('<int:id>/',views.blogPrice, name='blogPrice'),
    path('details/<str:name>/<int:age>/',views.details,name='details'),
]
