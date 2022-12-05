from . import views
from django.urls import path, include
app_name='todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:taskid>/', views.delete, name="delete"),
    path('cbvindex/', views.TaskListView.as_view(), name='cbvindex'),
    path('cbvdetails/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetails'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),
]
