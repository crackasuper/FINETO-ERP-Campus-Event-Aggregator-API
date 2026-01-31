

// import { useEffect, useState } from "react";
// import { fetchEvents } from "./api";


// function Events() {
//     const [events, setEvents] = useState([]);
//     const [source, setSource] = useState("");


//     useEffect(() => {
//         fetchEvents(source).then((res) => setEvents(res.data));
//     }, [source]);


//     return (
//         <div>
//             <h2>Upcoming Campus Events</h2>
//             <select onChange={(e) => setSource(e.target.value)}>
//                 <option value="">All</option>
//                 <option value="Source One">Source One</option>
//                 <option value="Source Two">Source Two</option>
//             </select>


//             <ul>
//                 {events.map((event, index) => (
//                     <li key={index}>
//                         <strong>{event.title}</strong>
//                         - {event.location} - {event.start_time}
//                     </li>
//                 ))}
//             </ul>
//         </div>
//     );
// }


// export default Events;


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
    <div style={{ padding: "20px" }}>
      <h2>Upcoming Campus Events</h2>

      <select onChange={(e) => setSource(e.target.value)}>
        <option value="">All</option>
        <option value="Source One">Source One</option>
        <option value="Source Two">Source Two</option>
      </select>

      <ul>
        {events.map((event, index) => (
          <li key={index}>
            <strong>{event.title}</strong> - {event.location} -{" "}
            {event.start_time}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Events;
