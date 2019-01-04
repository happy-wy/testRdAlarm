from django.urls import path
from testAlarm import views_if


app_name = 'testAlarm'

urlpatterns = [
    path('upload/add_Alarm', views_if.add_Alarm),
]