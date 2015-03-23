__author__ = 'mickeypash'

import os
from datetime import datetime
from faker import Factory
fake = Factory.create()

def populate():
    user = add_user(username=fake.first_name(), first_name=fake.first_name(), email=fake.email(), password=fake.state(), is_active=True)

    tag = add_tag(label=fake.word(), slug='portugal')

    note43 = add_note(title=fake.word(), timestamp=fake.date_time_this_year() , body=fake.paragraph(), tags=28)

    folder_astronomy = add_folder(title=fake.word(), owner=user)



# Defining the add functions for our models

# # Function for adding user to our model
def add_user(username, first_name, email, password, is_active):
    u = User.objects.get_or_create(username=username, first_name=first_name, email=email, password=password,
                                   is_active=is_active)[0]
    u.set_password(password)
    u.save()
    return u


# Fill in the param with attributes related to note (title, content, timestamp)
def add_note(title, timestamp, body, tags):
    # Look at add_user and how I have done it.
    n = Note.objects.get_or_create(title=title, timestamp=timestamp, body=body)[0]
    # You don't need to say n.save()
    return n


# Same applies for these two functions
def add_folder(title, owner):
    f = Folder.objects.get_or_create(title=title, owner=owner)[0]
    return f


def add_tag(label, slug):
    t = Tag.objects.get_or_create(label=label, slug=slug)[0]
    return t


# Start execution here!
## This is like public static void main(...) in Java
if __name__ == '__main__':
    ## Printing and importting necessary things
    print "Starting Pamm population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'noted.settings')
    from notes.models import Folder, Note, Tag
    from django.contrib.auth.models import User
    import django

    django.setup()

    # We are running the populate function we defined above
    populate()

    # If you are feeling adventurous you can make a class
    # which adds each model (i.e. a file populate_user etc.)
