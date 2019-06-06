# Run using ./manage.py update_db


from django.core.management.base import BaseCommand, CommandError

# Edit DB in 'external_script' app
from external_script.models import TestModel


class Command(BaseCommand):
    help = ''

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        name = "New Name3"

        # Save Record
        new_name = TestModel(name=name)
        new_name.save()
        print(f"Saved - '{name}' to TestModel database.")

        # Load Record
        load_name = TestModel.objects.filter(name=name).first()
        print(f"Loaded - '{load_name}' from TestModel database.")

        # Check if Successful
        if load_name == new_name:
            print("Successfully added and loaded record!")

            yn = input(
                f'Since this is confirmed working as intended, would you like to delete this newly created record for "{name}" ?(y/n)\n')

            if yn == "y":
                load_name.delete()
                print("Successfully deleted record. ")

        else:
            print("FAILED - 'Save' and 'Load' records did not match!")

        print("Script Complete!")


