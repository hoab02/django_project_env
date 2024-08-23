# urls.py
from django.urls import path
from .views import RobotDetailView, RobotListView, RobotCreateView

urlpatterns = [
    path('robots/', RobotListView.as_view(), name='robot-list'),
    path('robots/create/', RobotCreateView.as_view(), name='robot-create'),
    path('robots/<str:robot_id>/', RobotDetailView.as_view(), name='robot-detail')
]
