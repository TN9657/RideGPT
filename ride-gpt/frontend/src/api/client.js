import axios from 'axios'

const api = axios.create({ baseURL: '/api' })

export const requestRide = (data) => api.post('/ride/request', data).then(r => r.data)
export const getUserTrips = (userId) => api.get(`/trips/${userId}`).then(r => r.data)
export const getTripLogs = (tripId) => api.get(`/trip/${tripId}/logs`).then(r => r.data)
export const getAnalytics = (userId) => api.get(`/analytics/${userId}`).then(r => r.data)

export default api
