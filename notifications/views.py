from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Notification
from django.http import JsonResponse
from intimia_backend.settings import send_sms

@csrf_exempt
def send_notification(request):
    if request.method == 'POST':
        recipient = request.POST.get('recipient')
        message = request.POST.get('message')
        
        notification = Notification.objects.create(
            recipient=recipient,
            message=message
        )
        
        # Envoyer une notification par SMS
        send_sms(recipient.phone_number, message)
        
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

# from .models import Notification
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer

# from channels.generic.websocket import AsyncWebsocketConsumer
# from .models import Notification

# class NotificationConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         # Vérifier l'authentification de l'utilisateur
#         if self.scope["user"].is_anonymous:
#             await self.close()
#         else:
#             await self.channel_layer.group_add("notifications", self.channel_name)
#             await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard("notifications", self.channel_name)

#     async def receive(self, text_data):
#         # Rien à faire lors de la réception de données depuis le frontend
#         pass

#     async def send_notification(self, event):
#         notification = event["notification"]
#         await self.send(text_data=notification)


# def send_notification(request,message):
#     # Enregistrer la notification dans la base de données
#     notification = Notification.objects.create(user=request.user, message=message)

#     # Envoyer la notification à tous les utilisateurs connectés via le consumer
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)("notifications", {"type": "send_notification", "notification": str(notification)})

# @login_required
# @api_view(['POST'])
# def send_notification(request):
#     message = request.data.get('message')

#     if not message:
#         return Response({'error': 'Message is required'}, status=status.HTTP_400_BAD_REQUEST)

#     notification = Notification.objects.create(user=request.user, message=message)
#     serializer = NotificationSerializer(notification)

#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         f"user_{request.user.id}",
#         {
#             'type': 'notification',
#             'message': serializer.data
#         }
#     )

#     return Response(serializer.data, status=status.HTTP_201_CREATED)