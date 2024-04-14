import axios from 'axios';

let baseURL = 'http://localhost:8000/api/';

const httpClient = axios.create({ baseURL });

// Create a request interceptor

const requestInterceptor = httpClient.interceptors.request.use(
    config => {
        // Do something before request is sent
        return config;
    },
    error => {
        // Do something with request error
        console.log('Error here')
        return Promise.reject(error);
    }
);

// Create a response interceptor
const responseInterceptor = httpClient.interceptors.response.use(
    response => {
        return response;
    },
    error => {
        // Do something with response error
        if (error.response.status === 404) {
            console.log('404 Error: Page not found');
            // Handle the 404 error here
        }
        return Promise.reject(error);
    }
);

export default httpClient;