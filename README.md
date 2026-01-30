# FINETO-ERP-Campus-Event-Aggregator-API
### This project aggregates campus events from multiple external REST APIs, normalizes the data   into a unified schema, caches results to reduce repeated API calls, and exposes the data via a REST API consumed by a React frontend.

# 1. System Overview

Core Stack

Backend: Django + Django REST Framework

Frontend: React

Caching: Django Cache Framework (Redis recommended)

High-Level Architecture

External APIs → Aggregation Layer (Django Service) → Cache → REST Endpoint → React Frontend