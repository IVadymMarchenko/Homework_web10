from django.urls import path, include
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('author/<int:author_id>',views.author_data,name='author_detail')
]
