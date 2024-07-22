from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Create sequences for AutoIncrementField'

    def add_arguments(self, parser):
        parser.add_argument(
            '--sequence-names',
            nargs='+',
            help='List of sequence names to create',
        )

    def handle(self, *args, **options):
        sequence_names = options['sequence_names']
        if not sequence_names:
            self.stdout.write(
                self.style.ERROR('No sequence names provided. Use --sequence-names to specify sequence names.'))
            return

        with connection.cursor() as cursor:
            for name in sequence_names:
                cursor.execute(f"""
                    DO $$
                    BEGIN
                        IF NOT EXISTS (SELECT 1 FROM pg_class WHERE relkind = 'S' AND relname = '{name}') THEN
                            CREATE SEQUENCE {name};
                        END IF;
                    END
                    $$;
                """)
                self.stdout.write(self.style.SUCCESS(f'Sequence "{name}" created or already exists.'))
