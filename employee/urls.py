from django.urls import path
from .import views 
urlpatterns = [  
    #path('admin/', admin.site.urls),
    path('', views.show, name="show"),  
    path('emp/', views.emp, name="emp"),  
    path('show/',views.show, name="show"),  
    path('edit/<int:id>/', views.edit, name="edit"),  
    path('update/<int:id>/', views.update, name="update"),  
    path('delete/<int:id>/', views.destroy, name="delete"),
    path('search/', views.search, name="search"),  
]  