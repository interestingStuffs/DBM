import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import EventList from './components/EventList';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<EventList />} />
        {/* Add more routes as needed */}
      </Routes>
    </Router>
  );
}

export default App;
