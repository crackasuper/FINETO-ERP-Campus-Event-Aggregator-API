# FINETO – Campus Event Aggregator API

## Project Idea

The Campus Event Aggregator is a full‑stack application designed to collect campus events from multiple external REST APIs, normalize them into a single standard format, cache the results for performance, and present them through a clean React-based user interface.

The goal of the project is to demonstrate **ERP-style backend design**, API aggregation, caching strategy, and frontend consumption in a real-world scenario.

---

## Backend (Django + Django REST Framework)

### Responsibilities

* Consume multiple external event APIs
* Normalize event data into a unified schema
* Cache aggregated results to reduce repeated API calls
* Expose events through RESTful endpoints
* Allow admin users to manage events via Django Admin

### Core Technologies

* Django
* Django REST Framework
* Django Cache Framework
* Redis (for caching)

### Normalized Event Schema

All external event data is converted into the following internal format:

```json
{
  "title": "",
  "location": "",
  "start_time": "",
  "source": ""
}
```

### Data Flow

```
External APIs
   ↓
Aggregation & Normalization Layer
   ↓
Server-side Cache (Redis)
   ↓
REST API (/api/events/)
```

### Key API Endpoint

| Endpoint       | Method | Description                                 |
| -------------- | ------ | ------------------------------------------- |
| `/api/events/` | GET    | Returns aggregated and cached campus events |

---

## Frontend (React)

### Responsibilities

* Fetch events from the backend REST API
* Display upcoming campus events
* Filter events by source
* Provide a clean, professional UI

### Core Technologies

* React
* Axios
* Bootstrap

### Frontend Flow

```
React UI
   ↓
Axios API Calls
   ↓
Django REST API
```

---

## Caching Strategy

* Caching is implemented at the **aggregation layer** on the backend
* Aggregated events are cached for a fixed time period (e.g. 5 minutes)
* This reduces external API calls and improves response time

**Why caching here?**

* External APIs are slow and rate-limited
* Cached data can be reused across users
* Frontend filtering works on cached results

---

## Running the Project (Quick Start)

### Backend

```bash
python manage.py migrate
python manage.py runserver
```

### Frontend

```bash
npm install
npm start
```

---

## Summary

This project demonstrates:

* API aggregation and normalization
* Server-side caching using Redis
* Clean separation of backend and frontend
* ERP-style system design principles

The system is scalable, maintainable, and suitable for real-world enterprise applications.
