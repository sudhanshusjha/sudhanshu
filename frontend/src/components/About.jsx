import React from 'react';
import { CheckCircle, Award, Users, TrendingUp } from 'lucide-react';
import mockData from '../mock';

const About = () => {
  const { personal, about, certifications, achievements } = mockData;

  return (
    <section id="about" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid lg:grid-cols-2 gap-16 items-center">
          {/* Profile Image and Key Stats */}
          <div className="space-y-8">
            <div className="relative">
              <div className="w-80 h-80 mx-auto rounded-2xl overflow-hidden shadow-2xl">
                <img 
                  src={personal.profileImage}
                  alt={`${personal.name} - Professional Profile`}
                  className="w-full h-full object-cover"
                />
              </div>
              
              {/* Floating Stats Cards */}
              <div className="absolute -right-4 top-8 bg-white rounded-xl shadow-lg p-4 border">
                <div className="text-center">
                  <div className="text-2xl font-bold text-blue-600">{personal.yearsExperience}</div>
                  <div className="text-sm text-gray-600">Years Experience</div>
                </div>
              </div>
              
              <div className="absolute -left-4 bottom-8 bg-white rounded-xl shadow-lg p-4 border">
                <div className="text-center">
                  <div className="text-2xl font-bold text-green-600">6+</div>
                  <div className="text-sm text-gray-600">Certifications</div>
                </div>
              </div>
            </div>

            {/* Key Achievements */}
            <div className="grid grid-cols-2 gap-4">
              <div className="bg-blue-50 rounded-lg p-4 text-center">
                <TrendingUp className="w-8 h-8 text-blue-600 mx-auto mb-2" />
                <div className="text-sm font-medium text-blue-900">30% Cost Reduction</div>
                <div className="text-xs text-blue-700">Data Optimization</div>
              </div>
              <div className="bg-green-50 rounded-lg p-4 text-center">
                <Users className="w-8 h-8 text-green-600 mx-auto mb-2" />
                <div className="text-sm font-medium text-green-900">30% Engagement</div>
                <div className="text-xs text-green-700">Provider Platform</div>
              </div>
            </div>
          </div>

          {/* About Content */}
          <div className="space-y-8">
            <div>
              <h2 className="text-4xl font-light text-gray-900 mb-6">About Me</h2>
              <p className="text-lg text-gray-600 leading-relaxed mb-8">
                {about.summary}
              </p>
            </div>

            {/* Core Highlights */}
            <div className="space-y-4">
              <h3 className="text-xl font-semibold text-gray-900 mb-4">Core Expertise</h3>
              <div className="grid gap-3">
                {about.highlights.map((highlight, index) => (
                  <div key={index} className="flex items-start gap-3">
                    <CheckCircle className="w-5 h-5 text-green-500 mt-0.5 flex-shrink-0" />
                    <span className="text-gray-700">{highlight}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Certifications Grid */}
            <div className="space-y-4">
              <div className="flex items-center gap-2 mb-4">
                <Award className="w-5 h-5 text-blue-600" />
                <h3 className="text-xl font-semibold text-gray-900">Professional Certifications</h3>
              </div>
              <div className="grid grid-cols-2 gap-2">
                {certifications.map((cert, index) => (
                  <div key={index} className="bg-gray-50 rounded-lg px-3 py-2 text-sm text-gray-700 font-medium">
                    {cert}
                  </div>
                ))}
              </div>
            </div>

            {/* Awards */}
            <div className="space-y-4">
              <h3 className="text-xl font-semibold text-gray-900">Recognition & Awards</h3>
              <div className="space-y-3">
                {achievements.map((achievement, index) => (
                  <div key={index} className="border-l-4 border-blue-500 pl-4">
                    <h4 className="font-medium text-gray-900">{achievement.title}</h4>
                    <p className="text-sm text-gray-600">{achievement.description}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;