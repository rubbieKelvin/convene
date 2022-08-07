import axios from 'axios'

export default {
    url: import.meta.env.VITE_API_URL,
    async login() {
        try {
            const response = axios.post(`${this.url}/api/login`)
        } catch (e) {
            throw e
        }
    },
}