from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('crafts/', views.CraftList.as_view(), name="craft_list"),
    path('crafts/new/', views.CraftCreate.as_view(), name="craft_create"),
    path('crafts/<int:pk>/', views.CraftDetail.as_view(), name="craft_detail"),
    path('crafts/<int:pk>/update',views.CraftUpdate.as_view(), name="craft_update"),
    path('crafts/<int:pk>/delete',views.CraftDelete.as_view(), name="craft_delete")
]

