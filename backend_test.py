#!/usr/bin/env python3
"""
Comprehensive Backend API Tests for Sudhanshu's Portfolio Website
Tests all API endpoints with proper validation and error handling
"""

import requests
import json
import os
from datetime import datetime
from typing import Dict, Any

# Load environment variables
from dotenv import load_dotenv
load_dotenv('/app/frontend/.env')

# Get backend URL from environment
BACKEND_URL = os.getenv('REACT_APP_BACKEND_URL', 'https://tech-profile-30.preview.emergentagent.com')
API_BASE_URL = f"{BACKEND_URL}/api"

print(f"Testing backend API at: {API_BASE_URL}")

class PortfolioAPITester:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.session = requests.Session()
        self.test_results = []
        
    def log_test(self, test_name: str, success: bool, details: str = ""):
        """Log test results"""
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if details:
            print(f"   Details: {details}")
        
        self.test_results.append({
            "test": test_name,
            "success": success,
            "details": details,
            "timestamp": datetime.now().isoformat()
        })
    
    def test_health_check(self):
        """Test GET /api/ - Health check endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/")
            
            if response.status_code == 200:
                data = response.json()
                if "message" in data and "status" in data:
                    self.log_test("Health Check", True, f"Status: {data.get('status')}, Message: {data.get('message')}")
                    return True
                else:
                    self.log_test("Health Check", False, f"Missing required fields in response: {data}")
                    return False
            else:
                self.log_test("Health Check", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Health Check", False, f"Exception: {str(e)}")
            return False
    
    def test_portfolio_data(self):
        """Test GET /api/portfolio - Portfolio data endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/portfolio")
            
            if response.status_code == 200:
                data = response.json()
                
                # Validate required portfolio structure
                required_fields = ["id", "personal", "about", "skills", "experience", "projects", "certifications", "achievements"]
                missing_fields = [field for field in required_fields if field not in data]
                
                if missing_fields:
                    self.log_test("Portfolio Data Structure", False, f"Missing fields: {missing_fields}")
                    return False
                
                # Validate personal info
                personal = data.get("personal", {})
                personal_required = ["name", "title", "email", "phone", "linkedin"]
                personal_missing = [field for field in personal_required if field not in personal]
                
                if personal_missing:
                    self.log_test("Portfolio Personal Info", False, f"Missing personal fields: {personal_missing}")
                    return False
                
                # Validate Sudhanshu's specific data
                if personal.get("name") != "Sudhanshu Shekhar Jha":
                    self.log_test("Portfolio Data Validation", False, f"Incorrect name: {personal.get('name')}")
                    return False
                
                if personal.get("email") != "sudhanshurg@gmail.com":
                    self.log_test("Portfolio Data Validation", False, f"Incorrect email: {personal.get('email')}")
                    return False
                
                # Validate experience and projects arrays
                experience = data.get("experience", [])
                projects = data.get("projects", [])
                
                if not isinstance(experience, list) or len(experience) == 0:
                    self.log_test("Portfolio Experience", False, "Experience should be a non-empty array")
                    return False
                
                if not isinstance(projects, list) or len(projects) == 0:
                    self.log_test("Portfolio Projects", False, "Projects should be a non-empty array")
                    return False
                
                # Validate skills structure
                skills = data.get("skills", {})
                skills_required = ["productManagement", "programDelivery", "dataAndAI", "leadership", "technical"]
                skills_missing = [field for field in skills_required if field not in skills]
                
                if skills_missing:
                    self.log_test("Portfolio Skills", False, f"Missing skills categories: {skills_missing}")
                    return False
                
                self.log_test("Portfolio Data", True, f"Retrieved complete portfolio with {len(experience)} experiences and {len(projects)} projects")
                return True
                
            else:
                self.log_test("Portfolio Data", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Portfolio Data", False, f"Exception: {str(e)}")
            return False
    
    def test_contact_form_submission(self):
        """Test POST /api/contact - Contact form submission"""
        # Test data as specified in the review request
        test_contact_data = {
            "name": "John Smith",
            "email": "john.smith@techcorp.com",
            "company": "TechCorp Solutions",
            "message": "Hi Sudhanshu, I'm interested in discussing a Head of Product role at our company. Your experience with healthcare SaaS and Gen AI implementation is exactly what we need. Would you be available for a call next week?"
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/contact",
                json=test_contact_data,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # Validate response structure
                if "success" not in data or "message" not in data:
                    self.log_test("Contact Form Response", False, f"Missing required response fields: {data}")
                    return False
                
                if not data.get("success"):
                    self.log_test("Contact Form Submission", False, f"Submission failed: {data.get('message')}")
                    return False
                
                if "submissionId" not in data:
                    self.log_test("Contact Form Response", False, "Missing submissionId in response")
                    return False
                
                self.log_test("Contact Form Submission", True, f"Submission successful with ID: {data.get('submissionId')}")
                return data.get("submissionId")
                
            else:
                self.log_test("Contact Form Submission", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Contact Form Submission", False, f"Exception: {str(e)}")
            return False
    
    def test_contact_form_validation(self):
        """Test contact form validation with invalid data"""
        # Test missing required fields
        invalid_data_sets = [
            {"email": "test@test.com", "message": "Test message"},  # Missing name
            {"name": "Test User", "message": "Test message"},  # Missing email
            {"name": "Test User", "email": "test@test.com"},  # Missing message
            {"name": "Test User", "email": "invalid-email", "message": "Test message"},  # Invalid email
            {"name": "Test User", "email": "test@test.com", "message": "Short"},  # Message too short
        ]
        
        validation_passed = True
        
        for i, invalid_data in enumerate(invalid_data_sets):
            try:
                response = self.session.post(
                    f"{self.base_url}/contact",
                    json=invalid_data,
                    headers={"Content-Type": "application/json"}
                )
                
                # Should return 400 or 422 for validation errors
                if response.status_code in [400, 422]:
                    self.log_test(f"Contact Form Validation {i+1}", True, f"Correctly rejected invalid data: {response.status_code}")
                else:
                    self.log_test(f"Contact Form Validation {i+1}", False, f"Should have rejected invalid data but got: {response.status_code}")
                    validation_passed = False
                    
            except Exception as e:
                self.log_test(f"Contact Form Validation {i+1}", False, f"Exception: {str(e)}")
                validation_passed = False
        
        return validation_passed
    
    def test_contact_submissions_endpoint(self):
        """Test GET /api/contact/submissions - Admin endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/contact/submissions")
            
            if response.status_code == 200:
                data = response.json()
                
                # Validate response structure
                if "submissions" not in data or "count" not in data:
                    self.log_test("Contact Submissions", False, f"Missing required fields in response: {data}")
                    return False
                
                submissions = data.get("submissions", [])
                count = data.get("count", 0)
                
                if not isinstance(submissions, list):
                    self.log_test("Contact Submissions", False, "Submissions should be an array")
                    return False
                
                if len(submissions) != count:
                    self.log_test("Contact Submissions", False, f"Count mismatch: {len(submissions)} vs {count}")
                    return False
                
                # If we have submissions, validate structure
                if submissions:
                    first_submission = submissions[0]
                    required_fields = ["id", "name", "email", "message", "timestamp"]
                    missing_fields = [field for field in required_fields if field not in first_submission]
                    
                    if missing_fields:
                        self.log_test("Contact Submissions Structure", False, f"Missing fields in submission: {missing_fields}")
                        return False
                
                self.log_test("Contact Submissions", True, f"Retrieved {count} submissions")
                return True
                
            else:
                self.log_test("Contact Submissions", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Contact Submissions", False, f"Exception: {str(e)}")
            return False
    
    def test_analytics_endpoints(self):
        """Test optional analytics endpoints"""
        # Test page view logging
        try:
            page_view_data = {
                "page": "/",
                "referrer": "https://google.com"
            }
            
            response = self.session.post(
                f"{self.base_url}/analytics/page-view",
                json=page_view_data,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    self.log_test("Analytics Page View", True, "Page view logged successfully")
                else:
                    self.log_test("Analytics Page View", False, f"Failed to log page view: {data}")
            else:
                self.log_test("Analytics Page View", False, f"HTTP {response.status_code}: {response.text}")
                
        except Exception as e:
            self.log_test("Analytics Page View", False, f"Exception: {str(e)}")
        
        # Test analytics summary
        try:
            response = self.session.get(f"{self.base_url}/analytics/summary")
            
            if response.status_code == 200:
                data = response.json()
                required_fields = ["totalViews", "totalContacts", "topPages", "period"]
                missing_fields = [field for field in required_fields if field not in data]
                
                if missing_fields:
                    self.log_test("Analytics Summary", False, f"Missing fields: {missing_fields}")
                else:
                    self.log_test("Analytics Summary", True, f"Analytics summary retrieved for {data.get('period')}")
            else:
                self.log_test("Analytics Summary", False, f"HTTP {response.status_code}: {response.text}")
                
        except Exception as e:
            self.log_test("Analytics Summary", False, f"Exception: {str(e)}")
    
    def run_all_tests(self):
        """Run all backend API tests"""
        print("=" * 60)
        print("STARTING COMPREHENSIVE BACKEND API TESTS")
        print("=" * 60)
        
        # Core API tests
        self.test_health_check()
        self.test_portfolio_data()
        
        # Contact form tests
        submission_id = self.test_contact_form_submission()
        self.test_contact_form_validation()
        self.test_contact_submissions_endpoint()
        
        # Optional analytics tests
        self.test_analytics_endpoints()
        
        # Summary
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for result in self.test_results if result["success"])
        total = len(self.test_results)
        
        print(f"Total Tests: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {total - passed}")
        print(f"Success Rate: {(passed/total)*100:.1f}%")
        
        # List failed tests
        failed_tests = [result for result in self.test_results if not result["success"]]
        if failed_tests:
            print("\nFAILED TESTS:")
            for test in failed_tests:
                print(f"❌ {test['test']}: {test['details']}")
        
        return passed == total

if __name__ == "__main__":
    tester = PortfolioAPITester()
    success = tester.run_all_tests()
    
    if success:
        print("\n🎉 ALL TESTS PASSED! Backend API is working correctly.")
    else:
        print("\n⚠️  SOME TESTS FAILED! Check the details above.")
    
    exit(0 if success else 1)