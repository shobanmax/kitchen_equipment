from django.urls import path
from .views import *

urlpatterns = [
    path("",main,name="main"),
    path("spec/",spec,name="spec"),
    path("kick/",kick,name="kick"),
    path("run/",run,name="run"),
    path("pic/",pic,name="pic"),
    path("dev/",dev,name="dev"),
    
]