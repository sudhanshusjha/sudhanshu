import React, { useState, useEffect } from 'react';
import { ArrowRight, Download, ExternalLink } from 'lucide-react';
import { Button } from './ui/button';
import ApiService from '../services/api';

const Hero = () => {
  const [portfolioData, setPortfolioData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPortfolioData = async () => {
      try {
        setLoading(true);
        const data = await ApiService.getPortfolio();
        setPortfolioData(data);
        // Log page view for analytics
        ApiService.logPageView('hero');
      } catch (err) {
        setError(err.message);
        console.error('Failed to load portfolio data:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchPortfolioData();
  }, []);

  if (loading) {
    return (
      <section id="hero" className="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-50 to-white">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading portfolio...</p>
        </div>
      </section>
    );
  }

  if (error) {
    return (
      <section id="hero" className="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-50 to-white">
        <div className="text-center">
          <p className="text-red-600 mb-4">Error loading portfolio: {error}</p>
          <Button onClick={() => window.location.reload()}>
            Retry
          </Button>
        </div>
      </section>
    );
  }

  if (!portfolioData) {
    return null;
  }

  const { personal } = portfolioData;

  const scrollToContact = () => {
    const element = document.querySelector('#contact');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const scrollToProjects = () => {
    const element = document.querySelector('#projects');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section id="hero" className="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-50 to-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div className="text-center">
          {/* Main Content */}
          <div className="max-w-4xl mx-auto">
            <h1 className="text-5xl md:text-7xl font-light text-gray-900 mb-6 leading-tight">
              {personal.name}
            </h1>
            
            <div className="text-xl md:text-2xl text-gray-600 mb-4 font-medium">
              {personal.title}
            </div>
            
            <p className="text-lg md:text-xl text-gray-500 mb-8 max-w-2xl mx-auto leading-relaxed">
              {personal.tagline}
            </p>

            {/* Key Stats */}
            <div className="flex flex-wrap justify-center items-center gap-8 mb-12 text-gray-600">
              <div className="flex items-center gap-2">
                <span className="text-2xl font-bold text-blue-600">{personal.yearsExperience}</span>
                <span>Years Experience</span>
              </div>
              <div className="hidden sm:block w-px h-6 bg-gray-300"></div>
              <div className="text-center">
                <span className="text-sm font-medium">{personal.domain}</span>
              </div>
              <div className="hidden sm:block w-px h-6 bg-gray-300"></div>
              <div className="flex items-center gap-2">
                <span className="text-sm">{personal.location}</span>
              </div>
            </div>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
              <Button 
                onClick={scrollToProjects}
                className="bg-gray-900 hover:bg-gray-800 text-white px-8 py-3 rounded-lg text-lg font-medium transition-all duration-200 hover:scale-105 group"
              >
                View My Work
                <ArrowRight className="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </Button>
              
              <Button 
                variant="outline"
                onClick={scrollToContact}
                className="border-gray-300 text-gray-700 hover:bg-gray-50 px-8 py-3 rounded-lg text-lg font-medium transition-all duration-200 hover:scale-105"
              >
                Get In Touch
              </Button>
            </div>

            {/* Professional Note */}
            <div className="mt-16 pt-8 border-t border-gray-200">
              <p className="text-sm text-gray-500 max-w-3xl mx-auto leading-relaxed">
                Available for <span className="font-medium text-gray-700">Head/Director level roles</span> in 
                Technical Product Management, Program Management, and strategic consulting opportunities 
                with enterprise SaaS and healthcare technology companies.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;