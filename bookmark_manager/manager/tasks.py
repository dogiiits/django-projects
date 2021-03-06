import time
from celery import shared_task

from django.core.mail import send_mail


@shared_task
def sendmail():
    time.sleep(20)
    send_mail(
        subject='Thats your subject',
        message='That’s your message body',
        from_email='',
        recipient_list=['likhith@supplycompass.com', ],
        fail_silently=False,
    )
