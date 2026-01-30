
#this page handles event related services and api normalization

import requests

def normalize_event(title, location, start_time, source):
    return {
        "title": title,
        "location": location,
        "start_time": start_time,
        "spource": source,

    }


#defining two external mock APIs
SOURCE_A_API = "https://api.sourcea.com/events"
SOURCE_B_API = "https://api.sourceb.com/campus_events"