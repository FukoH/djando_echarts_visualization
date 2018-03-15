from django.urls import path
from  . import views



urlpatterns = [
    path('', views.hello),
    path('face',views.face),
    path('face_data',views.face_data)
]
