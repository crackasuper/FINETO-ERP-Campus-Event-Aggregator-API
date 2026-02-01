

import { useEffect, useState } from "react";
import { fetchEvents } from "./api";

function Events() {
  const [events, setEvents] = useState([]);
  const [source, setSource] = useState("");

  useEffect(() => {
    fetchEvents(source)
      .then((res) => setEvents(res.data))
      .catch((err) => console.error(err));
  }, [source]);

  return (
    <div className="container py-5">
      {/* Header */}
      <div className="mb-4 text-center">
        <h2 className="fw-bold">Campus Events</h2>
        <p className="text-muted">
          Aggregated events from multiple campus sources
        </p>
      </div>

      {/* Filter */}
      <div className="row mb-4">
        <div className="col-md-4">
          <select
            className="form-select"
            value={source}
            onChange={(e) => setSource(e.target.value)}
          >
            <option value="">All Sources</option>
            <option value="Source One">Source ONE</option>
            <option value="Source Two">Source TWO</option>
          </select>
        </div>
      </div>

      {/* Events */}
      <div className="row g-4">
        {events.length === 0 && (
          <p className="text-muted">No events available.</p>
        )}

        {events.map((event, index) => (
          <div className="col-md-6 col-lg-4" key={index}>
            <div className="card h-100 shadow-sm border-0">
              <div className="card-body">
                <h5 className="card-title fw-semibold">
                  {event.title}
                </h5>

                <p className="card-text mb-1">
                  📍 <span className="text-muted">{event.location}</span>
                </p>

                <p className="card-text mb-2">
                  🕒{" "}
                  <span className="text-muted">
                    {new Date(event.start_time).toLocaleString()}
                  </span>
                </p>

                <span className="badge bg-primary">
                  {event.source}
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Events;
