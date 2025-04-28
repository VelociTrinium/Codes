from django.urls import path
from . import views
from .views import get_students_json

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('rank/', views.rank_view, name='rank'),
    path('preferences/', views.preferences_view, name='preferences'),
    path('room_selection/', views.room_selection_view, name='room_selection'),
    path('api/preferences/students.json', get_students_json, name='get_students_json'),
    path('api/save_preference/', views.save_preference, name='save_preference'),

]
