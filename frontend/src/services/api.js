import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for logging
apiClient.interceptors.request.use(
  (config) => {
    console.log(`Making ${config.method?.toUpperCase()} request to ${config.url}`);
    return config;
  },
  (error) => {
    console.error('Request error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
apiClient.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

// API Service class
class ApiService {
  /**
   * Health check endpoint
   */
  static async healthCheck() {
    try {
      const response = await apiClient.get('/');
      return response.data;
    } catch (error) {
      throw new Error(`Health check failed: ${error.message}`);
    }
  }

  /**
   * Get complete portfolio data
   */
  static async getPortfolio() {
    try {
      const response = await apiClient.get('/portfolio');
      return response.data;
    } catch (error) {
      console.error('Error fetching portfolio data:', error);
      throw new Error(`Failed to fetch portfolio data: ${error.response?.data?.detail || error.message}`);
    }
  }

  /**
   * Submit contact form
   */
  static async submitContactForm(formData) {
    try {
      const response = await apiClient.post('/contact', formData);
      return response.data;
    } catch (error) {
      console.error('Error submitting contact form:', error);
      throw new Error(`Failed to submit contact form: ${error.response?.data?.detail || error.message}`);
    }
  }

  /**
   * Log page view for analytics (optional)
   */
  static async logPageView(page, referrer = null) {
    try {
      const response = await apiClient.post('/analytics/page-view', {
        page,
        referrer
      });
      return response.data;
    } catch (error) {
      // Don't throw error for analytics - just log it
      console.warn('Failed to log page view:', error.message);
      return null;
    }
  }

  /**
   * Get analytics summary (for admin use)
   */
  static async getAnalyticsSummary(days = 30) {
    try {
      const response = await apiClient.get(`/analytics/summary?days=${days}`);
      return response.data;
    } catch (error) {
      console.error('Error fetching analytics summary:', error);
      throw new Error(`Failed to fetch analytics summary: ${error.response?.data?.detail || error.message}`);
    }
  }

  /**
   * Get contact submissions (for admin use)
   */
  static async getContactSubmissions(limit = 50) {
    try {
      const response = await apiClient.get(`/contact/submissions?limit=${limit}`);
      return response.data;
    } catch (error) {
      console.error('Error fetching contact submissions:', error);
      throw new Error(`Failed to fetch contact submissions: ${error.response?.data?.detail || error.message}`);
    }
  }
}

export default ApiService;