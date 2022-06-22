""" apps/user/signals.py """
from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.dispatch import receiver # Import the receiver
from apps.user.models import Profile, Customer
from apps.cart.models import Cart


@receiver(post_save, sender=Customer) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        # creating profile  of a user
        Profile.objects.create(user=instance,
                            full_name=instance.full_name,
                            permanent_address=instance.address,
                            country=instance.country,
                            phone=instance.phone,
                            state=instance.state,
                            district=instance.district)
        # Creating cart of a user
        Cart.objects.create(user=instance)
