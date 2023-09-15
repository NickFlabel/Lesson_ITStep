from django.apps import AppConfig



class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from . import signals


# class PostSave:
#
#     list_of_subscribers = []
#
#     def notify(self):
#         for subscriber in self.list_of_subscribers:
#             subscriber(created, instance)
#
#     def connect(self, func):
#         self.list_of_subscribers.append(func)
#
#     def business_logic(self):
#         # new User saved
#         self.notify()
