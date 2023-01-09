from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"), #path converters <>
    path('labs',views.all_labs, name="list-labs"),
    path('show_lab/<lab_id>',views.show_lab, name="show-lab"),
    path('add_acad_div',views.add_acad_div, name="add-acad-div"),
    path('list_acad_divs',views.list_acad_divs, name="list-acad-divs"),
    path('show_acad_div/<acad_div_id>', views.show_acad_div, name='show-acad-div'),
    path('search_acad_divs',views.search_acad_divs, name="search-acad-divs"),
    path('update_acad_div/<acad_div_id>', views.update_acad_div, name='update-acad-div'),
    path('add_lab',views.add_lab, name="add-lab"),
]