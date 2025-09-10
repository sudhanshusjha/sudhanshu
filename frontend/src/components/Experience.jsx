import React from 'react';
import { MapPin, Calendar, ChevronRight } from 'lucide-react';
import mockData from '../mock';

const Experience = () => {
  const { experience } = mockData;

  return (
    <section id="experience" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16">
          <h2 className="text-4xl font-light text-gray-900 mb-4">Professional Journey</h2>
          <p className="text-lg text-gray-600 max-w-3xl mx-auto">
            18+ years of progressive growth from technical development to senior product and program leadership roles,
            consistently delivering measurable business impact across healthcare and enterprise SaaS domains.
          </p>
        </div>

        {/* Timeline */}
        <div className="relative">
          {/* Timeline Line */}
          <div className="absolute left-8 top-0 bottom-0 w-0.5 bg-gray-200 hidden md:block"></div>

          {/* Experience Items */}
          <div className="space-y-12">
            {experience.map((job, index) => (
              <div key={job.id} className="relative">
                {/* Timeline Dot */}
                <div className="absolute left-6 w-4 h-4 bg-blue-600 rounded-full border-4 border-white shadow-lg hidden md:block"></div>
                
                {/* Content */}
                <div className="md:ml-20 bg-white rounded-xl border border-gray-200 p-8 hover:shadow-lg transition-all duration-300 hover:-translate-y-1">
                  <div className="flex flex-col lg:flex-row lg:items-start lg:justify-between gap-4 mb-6">
                    <div className="flex-1">
                      <h3 className="text-xl font-semibold text-gray-900 mb-2">
                        {job.title}
                      </h3>
                      <div className="text-lg text-blue-600 font-medium mb-3">
                        {job.company}
                      </div>
                      <div className="flex flex-wrap items-center gap-4 text-gray-600">
                        <div className="flex items-center gap-1">
                          <MapPin className="w-4 h-4" />
                          <span className="text-sm">{job.location}</span>
                        </div>
                        <div className="flex items-center gap-1">
                          <Calendar className="w-4 h-4" />
                          <span className="text-sm">{job.duration}</span>
                        </div>
                        <span className="bg-gray-100 text-gray-700 px-2 py-1 rounded-full text-xs font-medium">
                          {job.type}
                        </span>
                      </div>
                    </div>
                  </div>

                  {/* Key Highlights */}
                  <div className="space-y-3">
                    <h4 className="text-lg font-medium text-gray-900 mb-4">Key Achievements</h4>
                    <div className="grid gap-3">
                      {job.highlights.map((highlight, highlightIndex) => (
                        <div key={highlightIndex} className="flex items-start gap-3">
                          <ChevronRight className="w-4 h-4 text-blue-600 mt-0.5 flex-shrink-0" />
                          <span className="text-gray-700 leading-relaxed">{highlight}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Career Progression Summary */}
        <div className="mt-16 bg-gradient-to-r from-blue-50 to-indigo-50 rounded-2xl p-8">
          <h3 className="text-2xl font-semibold text-gray-900 mb-6 text-center">
            Career Progression & Impact
          </h3>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="text-3xl font-bold text-blue-600 mb-2">18+</div>
              <div className="text-gray-700 font-medium">Years in Technology</div>
              <div className="text-sm text-gray-600 mt-1">From Developer to Senior Leader</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-green-600 mb-2">9+</div>
              <div className="text-gray-700 font-medium">Years in Product/Program</div>
              <div className="text-sm text-gray-600 mt-1">Leadership & Strategy Focus</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-purple-600 mb-2">5+</div>
              <div className="text-gray-700 font-medium">Healthcare SaaS Focus</div>
              <div className="text-sm text-gray-600 mt-1">Specialized Domain Expertise</div>
            </div>
          </div>
        </div>

        {/* Skills Evolution */}
        <div className="mt-12 text-center">
          <h4 className="text-lg font-semibold text-gray-900 mb-4">Evolution from Technical to Strategic Leadership</h4>
          <div className="flex flex-wrap justify-center items-center gap-2 max-w-4xl mx-auto">
            {[
              "Software Developer",
              "Technical Lead", 
              "Project Lead",
              "Technical Project Manager",
              "Senior Technical Product Manager",
              "Future: Head/Director Role"
            ].map((role, index) => (
              <React.Fragment key={index}>
                <span className="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm font-medium">
                  {role}
                </span>
                {index < 5 && <ChevronRight className="w-4 h-4 text-gray-400" />}
              </React.Fragment>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Experience;