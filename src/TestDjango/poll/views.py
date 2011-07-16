# Create your views here.
from django.http import HttpResponse
from models import Poll

def index(request):
    latestPolls = Poll.objects.order_by("-pub_date")[:5]
    output = '\n'.join( [p.question for p in latestPolls] )
    return HttpResponse( "My test response \n" + output )

def detail( request, poll_id ):
    return HttpResponse( "Search for poll id = " + poll_id )

def results( request, poll_id ):
    return HttpResponse( "Looking for results of poll = " + poll_id )

def vote( request, poll_id ):
    return HttpResponse( "Vote for poll " + poll_id )