from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

import time

from django.db.models.signals import post_save
from django.dispatch import receiver
from pet_products.models import Order
from pet_products.tasks import notify_user_about_new_order


@receiver(post_save, sender=Order)
def handle_order_created(instance: Order, created: bool = False, **kwargs):
    if not created:
        print("order", instance, "updated")
        return
    print("new order", instance, "created!, sending email")
    res = notify_user_about_new_order.delay(order_id=instance.pk)
    print("created task:", res)



