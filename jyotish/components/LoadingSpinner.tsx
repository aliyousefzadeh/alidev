
import React from 'react';

export const LoadingSpinner: React.FC = () => {
  return (
    <div className="flex flex-col items-center justify-center space-y-4">
      <div className="w-16 h-16 border-4 border-t-4 border-purple-400 border-t-transparent rounded-full animate-spin"></div>
      <p className="text-lg text-purple-300 font-semibold">Consulting the Cosmos...</p>
    </div>
  );
};
