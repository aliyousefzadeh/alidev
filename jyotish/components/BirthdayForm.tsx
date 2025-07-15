
import React, { useState } from 'react';
import { Birthday } from '../types';
import { ArrowRightIcon } from './icons';

interface BirthdayFormProps {
  onSubmit: (birthday: Birthday) => void;
  onBack: () => void;
}

export const BirthdayForm: React.FC<BirthdayFormProps> = ({ onSubmit, onBack }) => {
  const [day, setDay] = useState('');
  const [month, setMonth] = useState('');
  const [year, setYear] = useState('');
  const [error, setError] = useState<string | null>(null);

  const validateAndSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const yearNum = parseInt(year, 10);
    const monthNum = parseInt(month, 10);
    const dayNum = parseInt(day, 10);

    if (isNaN(yearNum) || isNaN(monthNum) || isNaN(dayNum)) {
      setError('Please fill in all fields with valid numbers.');
      return;
    }

    if (monthNum < 1 || monthNum > 12) {
      setError('Month must be between 1 and 12.');
      return;
    }
    
    if (dayNum < 1 || dayNum > 31) {
        setError('Day must be between 1 and 31.');
        return;
    }
    
    if (yearNum >= 1500 && yearNum <= 1900) {
      setError('Please enter a year before 1500 (for Persian calendar) or after 1900 (for Gregorian calendar).');
      return;
    }

    if (yearNum < 100 || yearNum > 2024) {
        setError('Please enter a realistic year.');
        return;
    }

    setError(null);
    onSubmit({ year: yearNum, month: monthNum, day: dayNum });
  };

  const InputField: React.FC<{
    label: string,
    value: string,
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void,
    placeholder: string
    maxLength: number
  }> = ({ label, value, onChange, placeholder, maxLength }) => (
    <div>
      <label className="block text-sm font-medium text-purple-300 mb-1">{label}</label>
      <input
        type="number"
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        maxLength={maxLength}
        className="w-full bg-gray-800/50 border border-gray-600 rounded-md p-3 text-white placeholder-gray-400 focus:ring-2 focus:ring-purple-500 focus:border-purple-500 outline-none transition"
      />
    </div>
  );

  return (
    <div className="max-w-md mx-auto text-center">
      <h2 className="text-3xl font-bold text-purple-300 mb-2">Enter Your Birth Date</h2>
      <p className="text-md text-gray-300 mb-6">This reveals the cosmic alignment at your time of birth.</p>
      <form onSubmit={validateAndSubmit} className="space-y-4">
        <div className="grid grid-cols-3 gap-4">
          <InputField label="Day" value={day} onChange={e => setDay(e.target.value)} placeholder="DD" maxLength={2} />
          <InputField label="Month" value={month} onChange={e => setMonth(e.target.value)} placeholder="MM" maxLength={2} />
          <InputField label="Year" value={year} onChange={e => setYear(e.target.value)} placeholder="YYYY" maxLength={4} />
        </div>

        {error && <p className="text-red-400 text-sm mt-2">{error}</p>}

        <div className="flex items-center justify-between pt-4">
          <button type="button" onClick={onBack} className="text-gray-300 hover:text-white transition">
            Back
          </button>
          <button
            type="submit"
            className="group inline-flex items-center justify-center px-6 py-3 bg-purple-600 text-white font-semibold rounded-lg hover:bg-purple-700 transition-colors duration-300 transform hover:scale-105 shadow-lg"
          >
            Generate Report
            <ArrowRightIcon className="w-5 h-5 ml-2 transition-transform group-hover:translate-x-1" />
          </button>
        </div>
      </form>
    </div>
  );
};
