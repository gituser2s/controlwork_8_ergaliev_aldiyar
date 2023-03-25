from django.contrib.auth.models import UserManager as BaseManager


class UserManager(BaseManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = username if not username else username
        return super().create_superuser(username, email, password, **extra_fields)