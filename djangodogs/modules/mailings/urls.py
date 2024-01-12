from django.urls import path

from .views import AnnouncementListView, AnnouncementDetailView

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='home'),
    path('announcements/<str:slug>/', AnnouncementDetailView.as_view(), name='announcements_detail'),
    path('send-broadcast/', AnnouncementDetailView.send_message, name='send_mess'),
]