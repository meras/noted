import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'noted.settings')

import django
django.setup()


from notes.models import Folder, Note, Tag

def populate():
     add_fold('Python',)

     add_fold('Java',)

     add_fold('Fortran')




    # Print out what we have added to the user.
   # for c in Category.objects.all():
   #     for p in Page.objects.filter(category=c):
   #        print "- {0} - {1}".format(str(c), str(p))


def add_fold(name,):
    f = Folder.objects.get_or_create(name=name)[0]
    return f

# Start execution here!
if __name__ == '__main__':
    print "Starting Notes population script..."
    populate()
