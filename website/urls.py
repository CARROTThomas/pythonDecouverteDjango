from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='home_index'),
    path("messages", views.all_messages, name='all_messages'),

    path("messages/create", views.create, name='create_message'),
    path("messages/update/<str:message_id>", views.update, name='update_message'),
    path("messages/show/<str:message_id>", views.show_message, name='show_message'),
    path("messages/delete/<str:message_id>", views.delete, name='delete_message'),
]