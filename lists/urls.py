from django.urls import path

from lists import views

app_name = 'lists'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('lists/new', views.new_list, name='new_list'),
    path('lists/<int:list_id>/', views.list_view, name='list_view'),
    path('lists/<int:list_id>/add_item', views.add_item, name='add_item')
]
