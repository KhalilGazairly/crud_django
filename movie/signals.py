from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Movie
from django.core.mail import send_mail


@receiver(post_delete, sender=Movie)
def notify_admins(**kwargs):
    instance = kwargs.get('instance')
    print("The deleted Movie is {}".format(instance))


# @receiver(post_save, sender=Movie)
# def my_handler(sender, instance, created, *args, **kwargs):
#     if created:
#         send_mail(
#             subject='Created New Movie Django Notification',
#             message='Hell Dear, See the last Movie from Django Movies {}'.format(instance.name),
#             from_email='zorro.tourry@gmail.com',
#             recipient_list=['khalil.gazairly@gmail.com'],
#             fail_silently=False
#         )
