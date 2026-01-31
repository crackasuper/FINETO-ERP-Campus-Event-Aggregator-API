
import axios from 'axios';

const API_URL = 'https://127.0.0.1:8000/events';


export const fetchEvents = (source) => {

  return axios.get(API_URL, {
    
        params: source ? { source } : {},

      });
};
 