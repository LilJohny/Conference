from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from conference.models import Presentation
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Create basic groups for app"

    # A command must define handle()
    def handle(self, *args, **options):
        new_group, created = Group.objects.get_or_create(name='Presenters')
        ct = ContentType.objects.get_for_model(Presentation)
        permission = Permission.objects.create(codename='can_create_presentations',
                                               name='Can create presentations',
                                               content_type=ct)
        new_group.permissions.add(permission)
