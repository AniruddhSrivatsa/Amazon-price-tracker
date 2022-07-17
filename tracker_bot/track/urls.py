from django.contrib import admin
from django.urls import path
from .views import home,LinkDeleteView,updating

urlpatterns=[
    path('admin/',admin.site.urls),
    path('',home,name='home'),
    path('delete/<pk>/',LinkDeleteView.as_view(), name='delete'),
    #path('change/<int:amaze_id>/',changed,name="change"),
    path('update/',updating,name="updates")
]

