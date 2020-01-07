# allows us to return information as an http response
from django.http import HttpResponse



# function for home page, we need to put a request in here
# whenever someone comes looking for something on our homepage, it sends this request object
def home(request):
    # we decide here what we are going to send back to the user, must be an http response
    return HttpResponse("Welcome to an original Django page!")

def candy(request):
    return HttpResponse("Can't take another egg example")

"""

Use templates to separate HTML code from view code

"""