from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Description of the command"

    def handle(self, *args, **options):
        self.stdout.write('This is my simple task')

