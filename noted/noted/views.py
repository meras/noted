from django.shortcuts import render

def landing(request):
    """
    View for the landing page of our project
    :return: Landing Page Template
    """
    return render(request, 'index.html')


def demo(request):
    """
    View just leads to a static page for demoing the WYSIWYG
    :return: Demo Template
    """
    return render(request, 'demo.html')

