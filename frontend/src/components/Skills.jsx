import React, { useState, useEffect } from 'react';
import { Target, Settings, BarChart3, Users2, Code } from 'lucide-react';
import ApiService from '../services/api';

const Skills = () => {
  const [portfolioData, setPortfolioData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPortfolioData = async () => {
      try {
        const data = await ApiService.getPortfolio();
        setPortfolioData(data);
        // Log page view for analytics
        ApiService.logPageView('skills');
      } catch (err) {
        console.error('Failed to load portfolio data:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchPortfolioData();
  }, []);

  if (loading) {
    return (
      <section id="skills" className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading skills information...</p>
        </div>
      </section>
    );
  }

  if (!portfolioData) {
    return null;
  }

  const { skills } = portfolioData;

  const skillCategories = [
    {
      title: "Product Management & Strategy",
      icon: Target,
      color: "blue",
      skills: skills.productManagement
    },
    {
      title: "Program & Delivery Management", 
      icon: Settings,
      color: "green",
      skills: skills.programDelivery
    },
    {
      title: "Data Analytics & Gen AI",
      icon: BarChart3,
      color: "purple",
      skills: skills.dataAndAI
    },
    {
      title: "Leadership & Stakeholder Management",
      icon: Users2,
      color: "orange",
      skills: skills.leadership
    },
    {
      title: "Technology & Tools",
      icon: Code,
      color: "gray",
      skills: skills.technical
    }
  ];

  const getColorClasses = (color) => {
    const colors = {
      blue: {
        bg: "bg-blue-50",
        icon: "text-blue-600",
        border: "border-blue-200",
        skill: "bg-blue-100 text-blue-800"
      },
      green: {
        bg: "bg-green-50", 
        icon: "text-green-600",
        border: "border-green-200",
        skill: "bg-green-100 text-green-800"
      },
      purple: {
        bg: "bg-purple-50",
        icon: "text-purple-600", 
        border: "border-purple-200",
        skill: "bg-purple-100 text-purple-800"
      },
      orange: {
        bg: "bg-orange-50",
        icon: "text-orange-600",
        border: "border-orange-200", 
        skill: "bg-orange-100 text-orange-800"
      },
      gray: {
        bg: "bg-gray-50",
        icon: "text-gray-600",
        border: "border-gray-200",
        skill: "bg-gray-100 text-gray-800"
      }
    };
    return colors[color];
  };

  return (
    <section id="skills" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16">
          <h2 className="text-4xl font-light text-gray-900 mb-4">Core Skills & Expertise</h2>
          <p className="text-lg text-gray-600 max-w-3xl mx-auto">
            A comprehensive blend of technical depth, product strategy, and leadership capabilities 
            honed over 18+ years in enterprise SaaS and healthcare technology domains.
          </p>
        </div>

        {/* Skills Grid */}
        <div className="grid lg:grid-cols-2 xl:grid-cols-3 gap-8">
          {skillCategories.map((category, index) => {
            const colors = getColorClasses(category.color);
            const IconComponent = category.icon;
            
            return (
              <div 
                key={index}
                className={`${colors.bg} rounded-xl p-6 border ${colors.border} hover:shadow-lg transition-all duration-300 hover:-translate-y-1`}
              >
                {/* Category Header */}
                <div className="flex items-start gap-4 mb-6">
                  <div className={`p-3 rounded-lg ${colors.skill}`}>
                    <IconComponent className={`w-6 h-6 ${colors.icon}`} />
                  </div>
                  <div>
                    <h3 className="text-lg font-semibold text-gray-900 mb-1">
                      {category.title}
                    </h3>
                  </div>
                </div>

                {/* Skills List */}
                <div className="flex flex-wrap gap-2">
                  {category.skills.map((skill, skillIndex) => (
                    <span 
                      key={skillIndex}
                      className={`px-3 py-1 rounded-full text-sm font-medium ${colors.skill} transition-all duration-200 hover:scale-105`}
                    >
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            );
          })}
        </div>

        {/* Professional Focus Areas */}
        <div className="mt-16 bg-white rounded-2xl p-8 shadow-sm border">
          <h3 className="text-2xl font-semibold text-gray-900 mb-6 text-center">
            Domain Expertise & Focus Areas
          </h3>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <Target className="w-8 h-8 text-blue-600" />
              </div>
              <h4 className="text-lg font-semibold text-gray-900 mb-2">Healthcare SaaS</h4>
              <p className="text-gray-600 text-sm">
                EHR analytics, HIPAA compliance, HL7/FHIR integration, clinical workflows
              </p>
            </div>
            <div className="text-center">
              <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <BarChart3 className="w-8 h-8 text-green-600" />
              </div>
              <h4 className="text-lg font-semibold text-gray-900 mb-2">Enterprise Data</h4>
              <p className="text-gray-600 text-sm">
                Data architecture, analytics platforms, Gen AI implementation, cost optimization
              </p>
            </div>
            <div className="text-center"> 
              <div className="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <Users2 className="w-8 h-8 text-purple-600" />
              </div>
              <h4 className="text-lg font-semibold text-gray-900 mb-2">Program Leadership</h4>
              <p className="text-gray-600 text-sm">
                Multi-team coordination, stakeholder management, delivery optimization
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Skills;