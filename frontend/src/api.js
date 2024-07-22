import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000'; // Adjust as needed

export const fetchEvents = async () => {
  const response = await axios.get(`${API_BASE_URL}/api/v1/events/`);
  return response.data;
};

export const postEvent = async (event) => {
  const response = await axios.post(`${API_BASE_URL}/api/v1/events/`, event);
  return response.data;
};