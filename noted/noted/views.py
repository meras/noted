from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def landing(request):
    """
    View for the landing page of our project
    :return: Landing Page Template
    """
    if request.user.is_authenticated():
        # If user is logged in show them their notes
        return HttpResponseRedirect(reverse('notes:index'))
    return render(request, 'index.html')


def demo(request):
    """
    View just leads to a static page for demoing the WYSIWYG
    :return: Demo Template
    """
    return render(request, 'demo.html')

