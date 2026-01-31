
#This page helps us to handle connection between urls and views
from django.urls import path
from .views import EventListView

urlpatterns = [
    path("events/", EventListView.as_view(), name="event-list")
]