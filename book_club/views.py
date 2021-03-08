from django.shortcuts import render


def book_club(request):
    """ A view to return the book club page with book reviews """

    return render(request, 'book_club/book_club.html')
