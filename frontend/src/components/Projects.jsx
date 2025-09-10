import React, { useState } from 'react';
import { ExternalLink, TrendingUp, Users, Brain, Activity, BarChart3 } from 'lucide-react';
import { Button } from './ui/button';
import mockData from '../mock';

const Projects = () => {
  const { projects } = mockData;
  const [selectedCategory, setSelectedCategory] = useState('All');

  const categories = ['All', 'Product Strategy & Analytics', 'Program Management & Operations', 'Innovation & AI Implementation', 'Healthcare Product Development', 'Data Analytics & Governance'];

  const filteredProjects = selectedCategory === 'All' 
    ? projects 
    : projects.filter(project => project.category === selectedCategory);

  const getCategoryIcon = (category) => {
    switch (category) {
      case 'Product Strategy & Analytics':
        return TrendingUp;
      case 'Program Management & Operations':
        return Activity;
      case 'Innovation & AI Implementation':
        return Brain;
      case 'Healthcare Product Development':
        return Users;
      case 'Data Analytics & Governance':
        return BarChart3;
      default:
        return TrendingUp;
    }
  };

  const getMetricDisplay = (project) => {
    const metrics = Object.entries(project.metrics);
    return metrics.slice(0, 3).map(([key, value]) => ({
      key: key.charAt(0).toUpperCase() + key.slice(1),
      value
    }));
  };

  return (
    <section id="projects" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16">
          <h2 className="text-4xl font-light text-gray-900 mb-4">Key Projects & Achievements</h2>
          <p className="text-lg text-gray-600 max-w-3xl mx-auto">
            Transformative initiatives that demonstrate strategic thinking, technical expertise, 
            and measurable business impact across healthcare SaaS and enterprise platforms.
          </p>
        </div>

        {/* Category Filter */}
        <div className="flex flex-wrap justify-center gap-2 mb-12">
          {categories.map((category) => (
            <Button
              key={category}
              variant={selectedCategory === category ? "default" : "outline"}
              onClick={() => setSelectedCategory(category)}
              className={`px-4 py-2 rounded-full text-sm font-medium transition-all duration-200 ${
                selectedCategory === category
                  ? 'bg-blue-600 text-white hover:bg-blue-700'
                  : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
              }`}
            >
              {category === 'All' ? 'All Projects' : category.split(' & ')[0]}
            </Button>
          ))}
        </div>

        {/* Projects Grid */}
        <div className="grid lg:grid-cols-2 gap-8">
          {filteredProjects.map((project) => {
            const IconComponent = getCategoryIcon(project.category);
            const displayMetrics = getMetricDisplay(project);
            
            return (
              <div
                key={project.id}
                className="bg-white rounded-xl shadow-sm hover:shadow-lg transition-all duration-300 hover:-translate-y-1 border border-gray-200"
              >
                {/* Project Header */}
                <div className="p-8 pb-6">
                  <div className="flex items-start justify-between mb-4">
                    <div className="flex items-start gap-4">
                      <div className="p-3 bg-blue-50 rounded-lg">
                        <IconComponent className="w-6 h-6 text-blue-600" />
                      </div>
                      <div className="flex-1">
                        <h3 className="text-xl font-semibold text-gray-900 mb-2">
                          {project.title}
                        </h3>
                        <span className="inline-block bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-xs font-medium">
                          {project.category}
                        </span>
                      </div>
                    </div>
                  </div>

                  <p className="text-gray-600 leading-relaxed mb-6">
                    {project.description}
                  </p>

                  {/* Key Metrics */}
                  <div className="grid grid-cols-3 gap-4 mb-6">
                    {displayMetrics.map((metric, index) => (
                      <div key={index} className="text-center bg-gray-50 rounded-lg p-3">
                        <div className="text-lg font-bold text-blue-600">{metric.value}</div>
                        <div className="text-xs text-gray-600">{metric.key}</div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Project Details */}
                <div className="p-8 pt-0">
                  {/* Achievements */}
                  <div className="mb-6">
                    <h4 className="text-sm font-semibold text-gray-900 mb-3">Key Achievements</h4>
                    <div className="grid gap-2">
                      {project.achievements.slice(0, 3).map((achievement, index) => (
                        <div key={index} className="flex items-start gap-2">
                          <div className="w-1.5 h-1.5 bg-green-500 rounded-full mt-2 flex-shrink-0"></div>
                          <span className="text-sm text-gray-700">{achievement}</span>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Technologies */}
                  <div className="mb-6">
                    <h4 className="text-sm font-semibold text-gray-900 mb-3">Technologies & Tools</h4>
                    <div className="flex flex-wrap gap-2">
                      {project.technologies.map((tech, index) => (
                        <span 
                          key={index}
                          className="bg-blue-50 text-blue-700 px-2 py-1 rounded text-xs font-medium"
                        >
                          {tech}
                        </span>
                      ))}
                    </div>
                  </div>

                  {/* Impact Statement */}
                  <div className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-lg p-4">
                    <h4 className="text-sm font-semibold text-gray-900 mb-2">Business Impact</h4>
                    <p className="text-sm text-gray-700 leading-relaxed italic">
                      "{project.impact}"
                    </p>
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        {/* Overall Impact Summary */}
        <div className="mt-16 bg-white rounded-2xl p-8 shadow-sm border">
          <h3 className="text-2xl font-semibold text-gray-900 mb-8 text-center">
            Cumulative Leadership Impact
          </h3>
          <div className="grid md:grid-cols-4 gap-8">
            <div className="text-center">
              <div className="text-3xl font-bold text-blue-600 mb-2">30%</div>
              <div className="text-gray-700 font-medium">Average Cost Reduction</div>
              <div className="text-sm text-gray-600 mt-1">Across optimization initiatives</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-green-600 mb-2">25%</div>
              <div className="text-gray-700 font-medium">Process Efficiency Gains</div>
              <div className="text-sm text-gray-600 mt-1">Through automation & AI</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-purple-600 mb-2">40%</div>
              <div className="text-gray-700 font-medium">Decision Speed Improvement</div>
              <div className="text-sm text-gray-600 mt-1">Executive dashboard systems</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-orange-600 mb-2">$2M+</div>
              <div className="text-gray-700 font-medium">Annual Cost Savings</div>
              <div className="text-sm text-gray-600 mt-1">Data & infrastructure optimization</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Projects;