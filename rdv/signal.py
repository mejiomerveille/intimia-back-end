from django.db.models.signals import post_save
from django.dispatch import receiver
from pyfcm import FCMNotification

@receiver(post_save, sender="Intimia")
def send_notification(sender, instance, created, **kwargs):
    if created:
        patient_token = instance.patient_notification_token
        doctor_token = instance.doctor_notification_token

        # Vérifiez si les tokens de notification sont disponibles
        if patient_token and doctor_token:
            # Configurez FCM avec votre clé d'API Firebase
            push_service = FCMNotification(api_key="AIzaSyAPqmeDMWNtRfdbg2l0zEKU7m4p4kR1xe8")

            # Construisez le message de notification
            message = {
                "token": patient_token,
                "notification": {
                    "title": "Rappel de rendez-vous médical",
                    "body": "Vous avez un rendez-vous médical le {date} à {time}."
                },
                "data": {
                    # Vous pouvez ajouter des données supplémentaires à envoyer avec la notification
                    "appointment_id": instance.id
                }
            }

            # Envoyez la notification au patient
            push_service.notify_single_device(**message)

            # Envoyez également la notification au médecin
            message["token"] = doctor_token
            push_service.notify_single_device(**message)