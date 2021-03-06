import os
from datetime import datetime
import random
from faker import Factory

fake = Factory.create()


def populate():
    user = add_user(username=fake.name(),
                    first_name=fake.first_name(),
                    email=fake.email(),
                    password=fake.state(),
                    is_active=True)

    tag = add_tag(label=fake.word(), slug='portugal')

    folder = add_folder(title=fake.word(), owner=user)

    text = ''
    for i in range(0,20):
        text += '<h2>' + fake.word() + '</h2>'
        text += '<p>'.join(fake.paragraphs())
        text += '</p>'

    note = add_note(title=fake.company(),
                    #author = user,
                    folder = folder,
                    timestamp=fake.date_time_this_year(),
                    body= text, tags=28)




# Defining the add functions for our models

# # Function for adding user to our model
def add_user(username, first_name, email, password, is_active):
    """


    :param username: string
    :param first_name: string
    :param email: string
    :param password: string (memorable yet secure)
    :param is_active: boolean
    :rtype : User Object
    """
    u = User.objects.get_or_create(username=username, first_name=first_name, email=email, password=password,
                                   is_active=is_active)[0]
    u.set_password(password)
    u.save()
    return u


def add_note(title, folder, timestamp, body, tags):
    """

    :param title: string
    :param timestamp: datetime
    :param body: string
    :param tags: a list? of Tag Objects?
    :return:
    """
    n = Note.objects.get_or_create(title=title,folder = folder,timestamp=timestamp, body=body)[0]
    return n


def add_folder(title, owner):
    """

    :param title: string
    :param owner: User Object
    :return: Folder Object
    """
    f = Folder.objects.get_or_create(title=title, owner=owner)[0]
    return f


def add_tag(label, slug):
    t = Tag.objects.get_or_create(label=label, slug=slug)[0]
    return t


# Start execution here!
# # This is like public static void main(...) in Java
if __name__ == '__main__':
    ## Printing and importing necessary things
    print "Starting NoteD population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'noted.settings')
    from notes.models import Note, Tag, Folder
    from django.contrib.auth.models import User
    import django

    django.setup()

    # We are running the populate function we defined above
    for i in range(0,10):
        fake.seed(random.random())
        populate()
