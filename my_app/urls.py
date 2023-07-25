from django.urls import path
from my_app import views

#
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    # path('<int:num_page>',views.num_page_view),
    # path('<str:topic>/',views.news_view,name='topic-page'),
]
