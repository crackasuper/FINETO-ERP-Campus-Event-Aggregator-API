from django.shortcuts import render

from django.core.cache import cache 
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import fetch_events_from_source_two, fetch_events_from_source_one

# Create your views here.

#defining catch key and timeout duration
CACHE_KEY = "aggregated_events"
CACHE_TIMEOUT = 300  #5 minutes

#preparing event listing view for aggregating events from multiple sources
def EventListView(APIView):
    def get(self, request):
        #checking if cached data exists
        events = cache.get(CACHE_KEY)

        #if the events does not exist in cache, fetch from sources
        if not events:
            source_one_events = fetch_events_from_source_one()
            source_two_events = fetch_events_from_source_two()
        
           #getting all events together
            events = source_one_events + source_two_events

            #storing aggregated events in cache
            cache.set(CACHE_KEY, events, CACHE_TIMEOUT)

        source_filter = request.query_params.get("source")
        if source_filter:
            events = [event for event in events if event["source"] == source_filter]
            
        return Response(events)

