from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Create sequences for AutoIncrementField with optional start value'

    def add_arguments(self, parser):
        parser.add_argument(
            '--sequence-names',
            nargs='+',
            help='List of sequence names to create',
        )
        parser.add_argument(
            '--start-values',
            nargs='+',
            type=int,
            help='List of start values for the sequences, corresponding to sequence names',
        )

    def handle(self, *args, **options):
        sequence_names = options['sequence_names']
        start_values = options['start_values'] or []

        if not sequence_names:
            self.stdout.write(
                self.style.ERROR('No sequence names provided. Use --sequence-names to specify sequence names.'))
            return

        if len(sequence_names) != len(start_values):
            self.stdout.write(self.style.ERROR('Number of sequence names must match number of start values.'))
            return

        with connection.cursor() as cursor:
            for name, start_value in zip(sequence_names, start_values):
                cursor.execute(f"""
                    DO $$
                    BEGIN
                        IF NOT EXISTS (SELECT 1 FROM pg_class WHERE relkind = 'S' AND relname = '{name}') THEN
                            CREATE SEQUENCE {name} START WITH {start_value};
                        END IF;
                    END
                    $$;
                """)
                self.stdout.write(
                    self.style.SUCCESS(f'Sequence "{name}" created with start value {start_value} or already exists.'))
