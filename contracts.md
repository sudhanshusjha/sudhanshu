# Portfolio Backend Integration Contracts

## Overview
This document outlines the API contracts and integration strategy for Sudhanshu's professional portfolio website, defining the transition from mock data to full backend functionality.

## Current Mock Data Structure (mock.js)
The frontend currently uses comprehensive mock data including:
- Personal information and profile details
- Skills organized by categories
- Work experience with achievements
- Project showcases with metrics
- Certifications and awards
- Contact information

## Backend Implementation Strategy

### 1. Portfolio Data Management
**Endpoint**: `GET /api/portfolio`
- **Purpose**: Serve complete portfolio data
- **Response**: JSON structure matching current mock.js format
- **Data Source**: MongoDB collection `portfolio_data`
- **Integration**: Replace mock.js imports with API calls

### 2. Contact Form Submission
**Endpoint**: `POST /api/contact`
- **Purpose**: Handle contact form submissions from potential employers/clients
- **Request Body**:
  ```json
  {
    "name": "string",
    "email": "string", 
    "company": "string",
    "message": "string",
    "timestamp": "datetime",
    "source": "portfolio_website"
  }
  ```
- **Response**: Success/error status with confirmation message
- **Features**: Email notifications, form validation, spam protection
- **Storage**: MongoDB collection `contact_submissions`

### 3. Analytics & Tracking (Optional)
**Endpoint**: `POST /api/analytics/page-view`
- **Purpose**: Track portfolio engagement for insights
- **Data**: Page views, section interactions, contact form submissions
- **Storage**: MongoDB collection `portfolio_analytics`

## Database Schema

### Portfolio Data Collection
```javascript
{
  _id: ObjectId,
  personal: {
    name: String,
    title: String,
    tagline: String,
    email: String,
    phone: String,
    location: String,
    profileImage: String,
    yearsExperience: String,
    domain: String
  },
  about: {
    summary: String,
    highlights: [String]
  },
  skills: {
    productManagement: [String],
    programDelivery: [String],
    dataAndAI: [String],
    leadership: [String],
    technical: [String]
  },
  experience: [{
    id: Number,
    title: String,
    company: String,
    location: String,
    duration: String,
    type: String,
    highlights: [String]
  }],
  projects: [{
    id: Number,
    title: String,
    category: String,
    description: String,
    achievements: [String],
    technologies: [String],
    impact: String,
    metrics: Object
  }],
  certifications: [String],
  achievements: [{
    title: String,
    description: String
  }],
  lastUpdated: Date
}
```

### Contact Submissions Collection
```javascript
{
  _id: ObjectId,
  name: String,
  email: String,
  company: String,
  message: String,
  timestamp: Date,
  source: String,
  status: String, // 'new', 'read', 'responded'
  ipAddress: String,
  userAgent: String
}
```

## Frontend Integration Changes

### 1. API Service Layer
- Create `src/services/api.js` for centralized API calls
- Replace mock.js imports with API service calls
- Add loading states and error handling

### 2. Component Updates
- **Hero.jsx**: Load personal data from API
- **About.jsx**: Load about, certifications, achievements from API  
- **Skills.jsx**: Load skills data from API
- **Experience.jsx**: Load experience data from API
- **Projects.jsx**: Load projects data from API
- **Contact.jsx**: Submit form data to backend API

### 3. State Management
- Add loading states for data fetching
- Implement error handling for API failures
- Add success/error feedback for contact form

## Implementation Priority

### Phase 1: Core Backend (Immediate)
1. MongoDB models for portfolio data and contact submissions
2. GET /api/portfolio endpoint
3. POST /api/contact endpoint with validation
4. Basic error handling and logging

### Phase 2: Frontend Integration (Immediate)
1. Create API service layer
2. Replace mock data with API calls
3. Add loading states and error handling
4. Update contact form to use backend

### Phase 3: Enhancements (Future)
1. Admin panel for portfolio updates
2. Email notifications for contact submissions
3. Analytics tracking
4. Performance optimization

## Testing Strategy
- Test all API endpoints with various input scenarios
- Verify contact form submission flow
- Test error handling and edge cases
- Validate data persistence in MongoDB
- Cross-browser compatibility testing

## Security Considerations
- Input validation and sanitization
- Rate limiting for contact form
- CORS configuration
- Data encryption for sensitive information
- Environment variable protection

This contract ensures seamless transition from mock data to full backend functionality while maintaining the professional user experience.