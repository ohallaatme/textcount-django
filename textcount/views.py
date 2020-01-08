# allows us to return information as an http response
from django.http import HttpResponse
# lets us bring in an HTML page to return
from django.shortcuts import render
from collections import Counter
import operator


# function for home page, we need to put a request in here
# whenever someone comes looking for something on our homepage, it sends this request object
def home(request):
    # we decide here what we are going to send back to the user, must be an http response
    # return HttpResponse("Welcome to an original Django page!")
    # Send people to a home HTML page
    return render(request, 'home.html')

# we pass in a request to render with user information
def count(request):
    # to get info from a request, use request.GET with key to parameter between
    # square brackets
    # fulltext is the name of the textarea in home.html
    full_text = request.GET['fulltext']
    # split function takes string and splits it into list of words based on space
    word_list = full_text.split()

    # Counter from collections to get count
    word_counts = Counter(word_list)

    word_dictionary = {}
    """ What word appeared the most """
    word_dictionary = dict(word_counts)


    # key=operator.itemgetter(1) is telling sorted() to look at the count
    # sorted() method turns into list of tuples
    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    print(full_text) # print will show up inside of terminal
    # pass fulltext to count page
    return render(request, 'count.html', {'fulltext':full_text, 'count': len(word_list),
                                          'sortedwords': sorted_words})


def about(request):
    return render(request, 'about.html')

"""
Use templates to separate HTML code from view code
"""