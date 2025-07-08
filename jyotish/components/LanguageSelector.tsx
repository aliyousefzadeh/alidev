
import React from 'react';
import { Language } from '../types';
import { LANGUAGES } from '../constants';

interface LanguageSelectorProps {
  onSelectLanguage: (language: Language) => void;
}

export const LanguageSelector: React.FC<LanguageSelectorProps> = ({ onSelectLanguage }) => {
  return (
    <div className="text-center">
      <h2 className="text-3xl font-bold text-purple-300 mb-2">Welcome, Seeker of Stars</h2>
      <p className="text-lg text-gray-300 mb-8">Begin your journey by selecting your language.</p>
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 max-w-md mx-auto">
        {LANGUAGES.map((lang) => (
          <button
            key={lang}
            onClick={() => onSelectLanguage(lang)}
            className="p-6 bg-white/5 border border-purple-500/30 rounded-lg text-xl font-semibold text-gray-200 hover:bg-purple-500/20 hover:border-purple-500 hover:text-white transition-all duration-300 transform hover:scale-105 shadow-lg"
          >
            {lang}
          </button>
        ))}
      </div>
    </div>
  );
};
