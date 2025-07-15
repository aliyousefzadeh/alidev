
import React from 'react';

interface AstrologyReportProps {
  report: string;
  onReset: () => void;
}

export const AstrologyReport: React.FC<AstrologyReportProps> = ({ report, onReset }) => {
  const formattedReport = report.split('\n').map((paragraph, index) => {
    // Basic formatting for headings
    if (paragraph.match(/^\d+\.\s+\*\*.+\*\*$/) || paragraph.match(/^\*\*.+\*\*$/)) {
      return <h3 key={index} className="text-2xl font-bold text-purple-300 mt-6 mb-3">{paragraph.replace(/\*|\d+\.\s/g, '')}</h3>;
    }
    return <p key={index} className="text-gray-300 leading-relaxed mb-4">{paragraph}</p>;
  });

  return (
    <div className="max-w-3xl mx-auto bg-white/5 border border-purple-500/30 rounded-xl p-6 sm:p-8 shadow-2xl backdrop-blur-sm">
      <h2 className="text-4xl font-bold text-center text-purple-200 mb-6">Your Vedic Horoscope</h2>
      <div className="prose prose-invert max-w-none prose-p:text-gray-300 prose-headings:text-purple-300">
        {formattedReport}
      </div>
      <div className="text-center mt-8">
        <button
          onClick={onReset}
          className="px-8 py-3 bg-purple-600 text-white font-semibold rounded-lg hover:bg-purple-700 transition-colors duration-300 transform hover:scale-105 shadow-lg"
        >
          Start Over
        </button>
      </div>
    </div>
  );
};
