
#this page handles event related services and api normalization

import requests

def normalize_event(title, location, start_time, source):
    return {
        "title": title,

        "location": location,

        "start_time": start_time,

        "source": source,

    }


#defining two external mock APIs
SOURCE_ONE_API = "https://api.sourcea.com/events"

SOURCE_TWO_API = "https://api.sourceb.com/campus_events"

''' handling external API request and overcoming application crash.

defining functions that fetches and normalizes events from first sources
'''
def fetch_events_from_source_one():
    try:
        response = requests.get(SOURCE_ONE_API, timeout=5) #5 seconds timeout
        response.raise_for_status()  # Raise an error for bad responses
        

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
    except requests.RequestException as e:
        print(f"Error fetching events from Source One: {e}")
        return [
            {
                "title": "Sample Event from source one",
                "location": "Sample Location",
                "start_time": "2026-02-01T00:00:00",
                "source": "Source One",
            }
        ]  # Return an empty list in case of error

#defining functions that fetches and normalizes events from second sources
def fetch_events_from_source_two():
    try:
        response = requests.get(SOURCE_TWO_API, timeout = 10) #10 seconds timeout
        response.raise_for_status()  # Raise an error for bad responses

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
    except requests.RequestException as e:
        print(f"Error fetching events from Source Two: {e}")
        return [
            {
                "title": "Sample Event from source two",
                "location": "Sample Location",
                "start_time": "2026-02-01T00:00:00",
                "source": "Source Two",
            }
        ]  # Return an empty list in case of error  

