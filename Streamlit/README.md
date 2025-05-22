Streamlit Dashboard for Solar and Wind Data Analysis

This project is a Streamlit dashboard designed to analyze and visualize data related to solar radiation, temperature, wind direction, and wind speed. The app allows users to dowload CSV files from drive, explore data trends, and visualize various components such as hourly and monthly averages, wind direction distributions, and correlation matrices for solar and temperature data.

Features Data download: Download your CSV files containing solar and wind data. Monthly Trends: Visualize monthly trends for solar radiation components (GHI, DNI, DHI) and temperature (Tamb). Hourly Averages: Explore hourly trends for solar radiation and temperature. Sensor Readings: Compare sensor readings for cleaned and not-cleaned data. Correlation Matrix: Display a heatmap showing the correlation between solar radiation components and temperature. Wind Direction Distribution: Analyze wind direction using a polar bar chart. Wind Speed Distribution: Visualize the distribution of wind speed using a radial bar chart.

Installation
git clone https://github.com/seid2015a/solar-challenge-week1.git

Install Required Dependencies: The dependencies required for this project are listed in the requirements.txt file. Install them using:

pip install -r requirements.txt

Run the Streamlit App: After installing the dependencies, you can run the app locally: streamlit run app.py

Contributing If you’d like to contribute to this project, feel free to open a pull request or submit issues for bug fixes or improvements. Contributions are welcome!