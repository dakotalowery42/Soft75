from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('Soft75Plan/', views.Soft75Plan, name = 'Soft75Plan'),
    path('Progress/', views.Progress, name = 'Progress'),
    path('Workout/', views.Workout, name = 'Workout'),
    # path('details/<int:id>', views.book_details, name = 'details')
]