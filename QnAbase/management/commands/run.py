# SKIPPING MIGRATION CHECKS!

# September 15, 2019 - 02:42:06
# Django version 2.2.5, using settings 'app.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CONTROL-C.


from django.core.management.commands.runserver import Command as RunServer

class Command(RunServer):

    def check(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("SKIPPING SYSTEM CHECKS!\n"))

    def check_migrations(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("SKIPPING MIGRATION CHECKS!\n"))