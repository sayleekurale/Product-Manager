from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from insights.models import SocialPost


class Command(BaseCommand):
    help = "Seed sample SocialPost data"

    def handle(self, *args, **options):
        user, _ = User.objects.get_or_create(username="demo")
        for i in range(10):
            SocialPost.objects.get_or_create(
                title=f"Post {i+1}",
                defaults={
                    "body": ("Lorem ipsum ") * (i + 1),
                    "author": user,
                },
            )
        self.stdout.write(self.style.SUCCESS("Seeded posts"))


