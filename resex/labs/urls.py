from django.urls import path, include
from . import views


urlpatterns = [

    #UUID: Universally Unique Identifier

    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('<int:year>/<str:month>/', views.home, name="home"), #path converters <>
    path('labs',views.all_labs, name="list-labs"),
    path('show_lab/<lab_id>',views.show_lab, name="show-lab"),
    path('add_acad_div',views.add_acad_div, name="add-acad-div"),
    path('list_acad_divs',views.list_acad_divs, name="list-acad-divs"),
    path('show_acad_div/<acad_div_id>', views.show_acad_div, name='show-acad-div'),
    path('search_acad_divs',views.search_acad_divs, name="search-acad-divs"),
    path('update_acad_div/<acad_div_id>', views.update_acad_div, name='update-acad-div'),
    path('add_lab',views.add_lab, name="add-lab"),
    path('update_lab/<lab_id>', views.update_lab, name='update-lab'),
    path('delete_lab/<lab_id>', views.delete_lab, name='delete-lab'),
    path('delete_acad_div/<acad_div_id>', views.delete_acad_div, name='delete-acad-div'),
    path('lab_csv', views.lab_csv, name='lab-csv'),
    path('my_labs', views.my_labs, name='my-labs'),
    path('search_labs', views.search_labs, name='search-labs'),
]