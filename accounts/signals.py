from django.db.models.signals import post_save, pre_init

from django.contrib.auth.models import User

from django.dispatch import receiver


from django.apps import apps


@receiver(post_save, sender=User)
def random_func(sender, **kwargs):
    if kwargs['created']:
        instance = kwargs['instance']
        author_model = apps.get_model('views_app', 'Author')
        author_model.objects.create(name=instance.username, bio='bio', email=instance.email, user=instance)
        print(f'Был создан новый автор по имени {instance.username}')


