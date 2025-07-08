
export enum Language {
  ENGLISH = 'English',
  PERSIAN = 'Persian',
  RUSSIAN = 'Russian',
  TURKISH = 'Turkish',
}

export interface Birthday {
  year: number;
  month: number;
  day: number;
}

export type CalendarType = 'Persian' | 'Gregorian';
