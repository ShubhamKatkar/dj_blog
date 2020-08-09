from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

# only add this method for signals

    def ready(self):
        import users.signals
