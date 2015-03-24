from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.

# def test_add_note

# def test_add_tag

def test_update_note(self):
    return True


# def test_slug_line_creation(self):
#     """
#     slug_line_creation checks to make sure that when we add a category an appropriate slug line is created
#     i.e. "Random Category String" -> "random-category-string"
#     """
#
#     folder = add_folder('Random Category String')
#     folder.save()
#     self.assertEqual(folder.slug, 'random-category-string')

class LandingViewTests(TestCase):

    def test_home_view_status_code(self):
        """
        Testing the response status codes
        Status expected - 200 OK
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class IndexViewTests(TestCase):

    def test_notes_index_view(self):
        """
        Testing the response status codes
        Status expected - 200 OK
        """
        response = self.client.get(reverse('notes:index'))
        self.assertEqual(response.status_code, 302)