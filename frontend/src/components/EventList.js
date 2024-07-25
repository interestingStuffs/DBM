import React, { useEffect, useState } from 'react';
import { fetchEvents } from '../api';

const EventList = () => {
  const [events, setEvents] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadEvents = async () => {
      try {
        const data = await fetchEvents();
        console.log('Fetched events:', data); // Log the data for debugging
        setEvents(data);
      } catch (err) {
        console.error('Error fetching events:', err);
        setError('Failed to load events');
      }
    };
    loadEvents();
  }, []);

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      <h1>Event List</h1>
      <ul>
        {events.map((event, index) => (
          <li key={index}>{event.name}</li> /* Use event.name instead of event.title */
        ))},
      </ul>
    </div>
  );
};

export default EventList;
