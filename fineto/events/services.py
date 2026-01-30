
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
SOURCE_ONE_API = "https://api.sourcea.com/events"

SOURCE_TWO_API = "https://api.sourceb.com/campus_events"


#defining functions that fetches and normalizes events from first sources
def fetch_events_from_source_one():
    response = requests.get(SOURCE_ONE_API, timeout=5) #5 seconds timeout

    data = response.json()

    return [
        {
            "title": event.get("name"),
            "location": event.get["venue"],
            "start_time": event.get["date"],
            "source": "Source One",
        }
        for event in data
    ]

#defining functions that fetches and normalizes events from second sources
def fetch_events_from_source_two():
    response = requests.get(SOURCE_TWO_API, timeout = 10) #10 seconds timeout

    data = response.json()

    return [
        {
            "title": event.get("title"),
            "location": event.get("location"),
            "start_time": event.get("start_time"),
            "source": "Source Two",
        }
        for event in data
    ]            

