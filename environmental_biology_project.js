
const axios = require("axios");

// Function to get environmental data
async function getEnvironmentalData(location) {
  try {
    // Make API request to retrieve environmental data
    const response = await axios.get(`https://api.environmentaldata.org/${location}`);
    
    // Process response data
    const { temperature, humidity, airQualityIndex } = response.data;
    
    // Print the environmental data
    console.log(`Environmental data for ${location}:`);
    console.log(`Temperature: ${temperature}°C`);
    console.log(`Humidity: ${humidity}%`);
    console.log(`Air Quality Index: ${airQualityIndex}`);
  } catch (error) {
    console.error(`Error retrieving environmental data: ${error.message}`);
  }
}

// Example usage
getEnvironmentalData("New York City");
getEnvironmentalData("Los Angeles");
