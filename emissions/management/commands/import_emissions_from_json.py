import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from emissions.models import Emission


class Command(BaseCommand):
    help = "Import greenhouse gas emissions data from a JSON file"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            type=str,
            default="emissions/seed_data/emissions.json",
            help="Path to the JSON file with emissions data",
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete existing Emission records before import",
        )

    def handle(self, *args, **options):
        file_path = Path(options["file"])

        if not file_path.exists():
            raise CommandError(f"File not found: {file_path}")

        self.stdout.write(self.style.NOTICE(f"Loading data from {file_path}"))

        with file_path.open("r", encoding="utf-8") as f:
            raw_data = json.load(f)

        if not isinstance(raw_data, list):
            raise CommandError("JSON root must be a list of emission records")

        if options["clear"]:
            self.stdout.write("Clearing existing Emission records...")
            Emission.objects.all().delete()

        emissions_to_create = []
        for idx, item in enumerate(raw_data, start=1):
            try:
                emissions_to_create.append(
                    Emission(
                        year=int(item["year"]),
                        emissions=item["emissions"],
                        emission_type=item["emission_type"],
                        country=item["country"],
                        activity=item["activity"],
                    )
                )
            except KeyError as e:
                raise CommandError(f"Missing field {e} in record #{idx}: {item}")

        Emission.objects.bulk_create(emissions_to_create, batch_size=500)

        self.stdout.write(
            self.style.SUCCESS(f"Imported {len(emissions_to_create)} emission records.")
        )
