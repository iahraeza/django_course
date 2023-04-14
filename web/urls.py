from django.urls import path
from . import views
urlpatterns = [
    path('post_view/', views.post_view, name='post_view'),
    path('<int:pk>/', views.post_detail,name="detail_view"),
    path("pub/", views.post_show_publish,name="post_show"),
    path("add/",views.postadd,name="postadd"),
    path("<int:pk>/update/",views.update_post,name="uppost"),
    path("<int:pk>/delete/",views.delete_post,name="deletepost"),
]
