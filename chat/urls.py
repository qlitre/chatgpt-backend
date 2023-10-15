from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('conversations/', views.ConversationList.as_view(), name='conversation_list'),
    path('conversations/create/', views.ConversationCreate.as_view(), name='conversation_create'),
    path('conversations/<int:pk>/', views.ConversationDetail.as_view(), name='conversation_detail'),
    path('conversations/<int:conversation_id>/messages/create/', views.MessageCreate.as_view(), name='message_create'),
    path('conversations/<int:conversation_id>/messages/create/ai/', views.AiMessageCreate.as_view(),
         name='ai_message_create'),
]
