# This script will interface with Django models without having to run the Django framework.

# Note: This script must be in Project ROOT directory to work. The other option it to use
#       "Management Commands" (see tutorial 'management_commands)


# Note: Add Environment
#     - This script will add the env details via code (found in project/wsgi.py)
#     - You can also add via below cmd
#         - `export DJANGO_SETTINGS_MODULE=tutorials.settings`
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorials.settings')
django.setup()

# Import Model
from external_script.models import TestModel

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

    yn = input(f'Since this is confirmed working as intended, would you like to delete this newly created record for "{name}" ?(y/n)\n')

    if yn == "y":
        load_name.delete()
        print("Successfully deleted record. ")

else:
    print("FAILED - 'Save' and 'Load' records did not match!")

print("Script Complete!")

