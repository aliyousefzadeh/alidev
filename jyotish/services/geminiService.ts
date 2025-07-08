
import { GoogleGenAI } from "@google/genai";
import { Birthday, CalendarType, Language } from '../types';

export const generateVedicReport = async (
  language: Language,
  birthday: Birthday,
  calendar: CalendarType
): Promise<string> => {
  if (!process.env.API_KEY) {
    throw new Error("API_KEY environment variable not set. Please ensure it is configured.");
  }

  const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });
  
  const { year, month, day } = birthday;

  const prompt = `
    You are an expert Vedic astrologer, deeply knowledgeable in Jyotish Shastra. 
    Your tone is wise, insightful, and supportive.
    Based on the following birth details, generate a comprehensive Vedic astrology chart analysis.
    
    **User's Birth Date:** ${day}/${month}/${year}
    **Calendar System Used:** ${calendar}
    **Language for the Report:** ${language}

    Please create a detailed and well-structured report covering the following aspects:

    1.  **Introduction:** A brief, welcoming introduction to Vedic astrology and what the user can expect from their reading.
    2.  **Personality Traits:** In-depth analysis of the person's core nature, strengths, and weaknesses based on their chart.
    3.  **Life Path (Dasha):** An overview of their destined life path and major life periods.
    4.  **Potential Challenges:** Identify possible challenges, obstacles, or karmic lessons they might encounter. Provide gentle advice on how to navigate them.
    5.  **Career Predictions:** Insights into suitable career paths, potential for success, and favorable periods for professional growth.
    6.  **Love and Relationships:** Analysis of their approach to love, compatibility factors, and predictions for their romantic life.
    7.  **Health and Wellness:** Astrological insights into potential health vulnerabilities and suggestions for maintaining well-being.
    8.  **Conclusion:** A summary of the key takeaways and a positive, encouraging final message.

    Structure the entire response in ${language}. Use clear headings for each section. Ensure the analysis is authentic to Jyotish Shastra principles.
  `;

  try {
    const response = await ai.models.generateContent({
        model: 'gemini-2.5-flash-preview-04-17',
        contents: prompt,
    });
    return response.text;
  } catch (error) {
    console.error("Error generating Vedic report:", error);
    if (error instanceof Error) {
        return `Failed to generate astrology report. Reason: ${error.message}`;
    }
    return "An unknown error occurred while generating the astrology report.";
  }
};
