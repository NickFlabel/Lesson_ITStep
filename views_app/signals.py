from django.db.models.signals import post_save, pre_init, post_init, pre_save, pre_delete, post_delete, m2m_changed
from django.core.signals import request_started, request_finished, got_request_exception
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver, Signal

from .models import Author, Post, Category

# pre_init - Сигнал, который направляется в начале создании новой записи модели - перед выполнением конструктора ее класса
# Author(name='author')
# kwargs ['args']


@receiver(pre_init, sender=Author)
def author_pre_init(sender, args, **kwargs):
    print(f"Pre-init: Author instance с аргументами {args}")


@receiver(post_init, sender=Author)
def author_post_init(sender, instance, **kwargs):
    print(f"Post_init: Author instance initialized с именем {instance.name}")


@receiver(pre_save, sender=Author)
def author_pre_save(sender, instance, **kwargs):
    print(f"Pre_save: Author instance with name {instance.name} is about to be saved")


@receiver(post_save, sender=Author)
def author_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"Post_save: new Author instance with name {instance.name} was saved")
    else:
        print(f"Post_save: existing Author instance with name {instance.name} was updated")


@receiver(pre_delete, sender=Author)
def author_pre_delete(sender, instance, **kwargs):
    print(f"Pre_delete: Author instance with name {instance.name} is about to be deleted")


@receiver(post_delete, sender=Author)
def author_post_delete(sender, instance, **kwargs):
    print(f"Post_delete: Author instance with name {instance.name} has been deleted")


@receiver(m2m_changed, sender=Post.categories.through)
def post_categories_changed(sender, instance, action, model, pk_set, **kwargs):
    if action == 'post_add':
        print(f"Categories added to post {instance.title}: {' '.join(str(Category.objects.get(pk=pk)) for pk in pk_set)}")
    if action == 'post_remove':
        print(f"Categories removed to post {instance.title}: {' '.join(str(Category.objects.get(pk=pk)) for pk in pk_set)}")


@receiver(request_started)
def request_started_handler(sender, environ, **kwargs):
    print(f"Запрос принят")


@receiver(request_finished)
def request_finished_handler(sender, **kwargs):
    print(f'Запрос обработан')


@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    print(f"User {user.username} has logged in")


@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    print(f"User {user.username} has logged out")


@receiver(user_login_failed)
def user_login_failed_handler(sender, credentials, request, **kwargs):
    print(f"User {credentials} has failed to log in")


@receiver(got_request_exception)
def got_request_exception_handler(sender, request, **kwargs):
    print(f'Error when trying to handle request: {request}')


my_signal = Signal()


@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print(f'Custom signal by {sender} received!')
    print(f'Received request from {sender.request.user}')
    print(f'{sender.template_name}')
    print(f"{kwargs['context']}")
