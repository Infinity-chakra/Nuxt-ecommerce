import os
from django.core.management.base import BaseCommand
from django.db import connections

class Command(BaseCommand):
    help = 'Creates a backup of the database.'

    def add_arguments(self, parser):
        parser.add_argument('--filename', type=str, default='db_backup.sql',
                            help='Filename for the backup (default: db_backup.sql)')
        parser.add_argument('--database', type=str, default=None,
                            help='Specific database to backup (default: all)')

    def handle(self, *args, **options):
        filename = options['filename']
        database = options['database']

        # Get database connection details
        if database:
            connection = connections[database]
        else:
            connection = connections['default']
        db_engine = connection.vendor
        db_name = connection.settings_dict['NAME']
        db_user = connection.settings_dict['USER']
        db_password = connection.settings_dict['PASSWORD']
        db_host = connection.settings_dict['HOST']
        db_port = connection.settings_dict['PORT']


        # # Construct command based on database engine
        if db_engine == 'postgresql':
            command = f"pg_dump -h {db_host} -p {db_port} -U {db_user} -W {db_password} {db_name} > {filename}"
        elif db_engine == 'mysql':
            command = f"mysqldump -h {db_host} -P {db_port} -u {db_user} -p{db_password} {db_name} > {filename}"
        else:
            raise NotImplementedError(f"Database engine '{db_engine}' not supported")

        # Execute the backup command
        with os.popen(command) as pipe:
            output = pipe.read()
            if output:
                self.stdout.write(f"Backup failed:\n{output}")
            else:
                self.stdout.write(f"Database backup '{filename}' created successfully.")
