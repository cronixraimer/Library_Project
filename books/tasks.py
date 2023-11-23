from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

@shared_task
def send_welcome_email(user_id):
    user = get_user_model().objects.get(pk=user_id)
    send_mail(
        'Welcome to My Library',
        'Thank you for registering!',
        'from@example.com',
        [user.email],
        fail_silently=False,
    )
