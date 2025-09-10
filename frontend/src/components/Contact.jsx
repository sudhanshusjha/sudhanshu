import React, { useState, useEffect } from 'react';
import { Mail, Phone, MapPin, Linkedin, Download } from 'lucide-react';
import { Button } from './ui/button';
import ApiService from '../services/api';

const Contact = () => {
  const [portfolioData, setPortfolioData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPortfolioData = async () => {
      try {
        const data = await ApiService.getPortfolio();
        setPortfolioData(data);
        // Log page view for analytics
        ApiService.logPageView('contact');
      } catch (err) {
        console.error('Failed to load portfolio data:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchPortfolioData();
  }, []);

  if (loading || !portfolioData) {
    return (
      <section id="contact" className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading contact information...</p>
        </div>
      </section>
    );
  }

  const { personal } = portfolioData;

  const contactMethods = [
    {
      icon: Mail,
      label: 'Email',
      value: personal.email,
      href: `mailto:${personal.email}`,
      color: 'blue'
    },
    {
      icon: Phone,
      label: 'Phone',
      value: personal.phone,
      href: `tel:${personal.phone}`,
      color: 'green'
    },
    {
      icon: MapPin,
      label: 'Location',
      value: personal.location,
      href: '#',
      color: 'purple'
    },
    {
      icon: Linkedin,
      label: 'LinkedIn',
      value: 'Connect on LinkedIn',
      href: personal.linkedin,
      color: 'blue'
    }
  ];

  return (
    <section id="contact" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16">
          <h2 className="text-4xl font-light text-gray-900 mb-4">Let's Connect</h2>
          <p className="text-lg text-gray-600 max-w-3xl mx-auto">
            Open to discussing Head/Director level opportunities in Technical Product Management, 
            Program Management, strategic consulting, and thought leadership collaborations.
          </p>
        </div>

        <div className="max-w-4xl mx-auto">
          {/* Contact Information */}
          <div className="space-y-8">
            <div>
              <h3 className="text-2xl font-semibold text-gray-900 mb-6 text-center">Get In Touch</h3>
              <p className="text-gray-600 leading-relaxed mb-8 text-center">
                Whether you're looking for senior product leadership, program management expertise, 
                or strategic consulting in healthcare SaaS and enterprise technology domains, 
                I'd love to explore how we can work together.
              </p>
            </div>

            {/* Contact Methods Grid */}
            <div className="grid md:grid-cols-2 gap-6 mb-12">
              {contactMethods.map((method, index) => {
                const IconComponent = method.icon;
                return (
                  <a
                    key={index}
                    href={method.href}
                    target={method.label === 'LinkedIn' ? '_blank' : '_self'}
                    rel={method.label === 'LinkedIn' ? 'noopener noreferrer' : ''}
                    className="flex items-center gap-6 p-6 bg-gray-50 rounded-xl hover:bg-gray-100 transition-colors group hover:shadow-md"
                  >
                    <div className={`p-4 rounded-xl ${
                      method.color === 'blue' ? 'bg-blue-100 text-blue-600' :
                      method.color === 'green' ? 'bg-green-100 text-green-600' :
                      method.color === 'purple' ? 'bg-purple-100 text-purple-600' :
                      'bg-gray-100 text-gray-600'
                    }`}>
                      <IconComponent className="w-6 h-6" />
                    </div>
                    <div>
                      <div className="font-semibold text-gray-900 group-hover:text-blue-600 transition-colors text-lg">
                        {method.label}
                      </div>
                      <div className="text-gray-600 mt-1">
                        {method.value}
                      </div>
                    </div>
                  </a>
                );
              })}
            </div>

            {/* Professional Availability */}
            <div className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-8 border border-blue-200">
              <h4 className="font-semibold text-blue-900 mb-4 text-xl text-center">Current Availability</h4>
              <div className="grid md:grid-cols-3 gap-6 text-blue-800">
                <div className="text-center">
                  <div className="w-3 h-3 bg-green-500 rounded-full mx-auto mb-2"></div>
                  <span className="text-sm font-medium">Open to Head/Director level opportunities</span>
                </div>
                <div className="text-center">
                  <div className="w-3 h-3 bg-green-500 rounded-full mx-auto mb-2"></div>
                  <span className="text-sm font-medium">Available for strategic consulting projects</span>
                </div>
                <div className="text-center">
                  <div className="w-3 h-3 bg-green-500 rounded-full mx-auto mb-2"></div>
                  <span className="text-sm font-medium">Speaking & thought leadership opportunities</span>
                </div>
              </div>
            </div>

            {/* Resume Download */}
            <div className="text-center">
              <Button 
                variant="outline"
                className="border-gray-300 text-gray-700 hover:bg-gray-50 px-8 py-4 rounded-xl font-medium transition-all duration-200 hover:scale-105 text-lg"
              >
                <Download className="w-5 h-5 mr-3" />
                Download Resume
              </Button>
            </div>

            {/* Professional Note */}
            <div className="text-center mt-12 pt-8 border-t border-gray-200">
              <p className="text-sm text-gray-500 max-w-2xl mx-auto leading-relaxed">
                <span className="font-medium text-gray-700">Response Time:</span> Typically within 24 hours for professional inquiries.
                Available for immediate start on the right opportunity.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Contact;