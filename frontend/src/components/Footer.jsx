import React from 'react';
import { Linkedin, Mail, Phone } from 'lucide-react';
import mockData from '../mock';

const Footer = () => {
  const { personal } = mockData;
  const currentYear = new Date().getFullYear();

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer className="bg-gray-900 text-white py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid md:grid-cols-3 gap-8">
          {/* Professional Summary */}
          <div className="space-y-4">
            <h3 className="text-xl font-semibold">{personal.name}</h3>
            <p className="text-gray-300 leading-relaxed">
              Senior Technical Product & Program Manager specializing in healthcare SaaS, 
              enterprise data platforms, and Gen AI-powered solutions.
            </p>
            <div className="text-sm text-gray-400">
              {personal.yearsExperience} years experience • {personal.location}
            </div>
          </div>

          {/* Quick Links */}
          <div className="space-y-4">
            <h4 className="text-lg font-semibold">Professional Focus</h4>
            <div className="space-y-2 text-gray-300">
              <div>• Technical Product Management</div>
              <div>• Program & Delivery Leadership</div>
              <div>• Healthcare SaaS Platforms</div>
              <div>• Gen AI Implementation</div>
              <div>• Strategic Consulting</div>
            </div>
          </div>

          {/* Contact & Connect */}
          <div className="space-y-4">
            <h4 className="text-lg font-semibold">Let's Connect</h4>
            <div className="space-y-3">
              <a 
                href={`mailto:${personal.email}`}
                className="flex items-center gap-3 text-gray-300 hover:text-white transition-colors group"
              >
                <Mail className="w-4 h-4" />
                <span className="group-hover:underline">{personal.email}</span>
              </a>
              <a 
                href={`tel:${personal.phone}`}
                className="flex items-center gap-3 text-gray-300 hover:text-white transition-colors group"
              >
                <Phone className="w-4 h-4" />
                <span className="group-hover:underline">{personal.phone}</span>
              </a>
              <a 
                href={personal.linkedin}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-3 text-gray-300 hover:text-white transition-colors group"
              >
                <Linkedin className="w-4 h-4" />
                <span className="group-hover:underline">LinkedIn Profile</span>
              </a>
            </div>

            {/* Professional Newsletter */}
            <div className="bg-gray-800 rounded-lg p-4 mt-6">
              <h5 className="font-medium text-white mb-2">Tech PMx Junction</h5>
              <p className="text-sm text-gray-400">
                Professional newsletter sharing real-world lessons in product, project, and program management.
              </p>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="border-t border-gray-800 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center">
          <div className="text-gray-400 text-sm">
            © {currentYear} {personal.name}. All rights reserved.
          </div>
          <div className="flex items-center gap-6 mt-4 md:mt-0">
            <button
              onClick={scrollToTop}
              className="text-gray-400 hover:text-white text-sm transition-colors hover:underline"
            >
              Back to Top
            </button>
            <div className="text-gray-400 text-sm">
              Available for senior leadership roles
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;