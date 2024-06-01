from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

from app.models import UserType

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(email=settings.SUPERUSER_EMAIL).exists():
            User.objects.create_superuser(
                email=settings.SUPERUSER_EMAIL,
                password=settings.SUPERUSER_PASSWORD,
                first_name=settings.SUPERUSER_FIRST_NAME,
                last_name=settings.SUPERUSER_LAST_NAME,
                user_type=UserType.SUPPORTER,
            )
            print("スーパーユーザー作成")
