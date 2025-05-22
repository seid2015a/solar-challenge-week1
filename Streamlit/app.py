import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import gdown 

# Set Streamlit page configuration
st.set_page_config(page_title="Simple Dashboard", layout="wide")

# Sidebar option
with st.sidebar:
    selected_option = st.radio("Select an option:", ["Data Upload", "Monthly trends", "Display Hourly Averages", "Sensor Reading","Correlation matrix for solar radiation and temperature","Wind Direction Distribution","Wind Speed Distribution"])

# Main Title
st.title("Streamlit Dashboard")

# drive location of csv files
togo= "https://drive.google.com/file/d/1LcaKQPMLsdubohoaALe26PwhXdU3Bjr8/view?usp=drive_link"
benin = "https://drive.google.com/file/d/1XK-J9gapOFsqqhjp8zxr-8cuqQ-YWuf9/view?usp=drive_link"
seralion = "https://drive.google.com/file/d/1hap-TpUy0b8PHPBDRjQogvVy89_fEO-S/view?usp=sharing"

togo_dapaong_qc=f"https://drive.google.com/uc?id={togo.split('/')[-2]}"
benin_malanvile=f"https://drive.google.com/uc?id={benin.split('/')[-2]}"
sierraleon_bumbana=f"https://drive.google.com/uc?id={seralion.split('/')[-2]}"


# File uploader (accessible in all options)
#uploaded_file = st.file_uploader("Choose a CSV file to upload", type="csv")
file= st.radio("choose a csv file found in drive:",[benin_malanvile,sierraleon_bumbana,togo_dapaong_qc])
uploaded_file="uploaded_file.csv"
gdown.download(file,uploaded_file,quiet=False)

# Option 1: Download CSV and Plot Data
if selected_option == "Data Upload":
    st.header("Download CSV and Plot Data")
    if uploaded_file is not None:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(uploaded_file)

        # Display the first 5 rows of the DataFrame (preview first 19 columns)
        st.subheader("Downloaded Data Preview")
        st.write(data.iloc[:5, :19])  # Select first 5 rows and up to 19 columns
    else:
        st.warning("Please Download a CSV file to display the data.")

# Option 2: Monthly trends
elif selected_option == "Monthly trends":
    st.header("Monthly Trends")

    if uploaded_file is not None:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(uploaded_file)

        # Ensure the 'Timestamp' column is a datetime object
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])

        # Extract time-based features
        data['Month'] = data['Timestamp'].dt.month

        # Calculate monthly averages
        if all(col in data.columns for col in ['GHI', 'DNI', 'DHI', 'Tamb']):
            monthly_avg = data.groupby('Month')[['GHI', 'DNI', 'DHI', 'Tamb']].mean()

            # Plotting monthly trends
            plt.figure(figsize=(14, 8))
            plt.subplot(2, 1, 1)
            monthly_avg.plot(kind='bar', ax=plt.gca(), colormap='viridis', alpha=0.8)
            plt.title("Monthly Averages of GHI, DNI, DHI, and Tamb")
            plt.ylabel("Values")
            plt.xlabel("Month")
            plt.xticks(ticks=range(12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
            plt.legend(loc='upper left')

            # Display the plot
            st.pyplot(plt)
        else:
            st.warning("The CSV file is missing necessary columns: 'GHI', 'DNI', 'DHI', or 'Tamb'.")
    else:
        st.warning("Please Download a CSV file to view the monthly trends plot.")

# Option 3: Display Hourly Averages
elif selected_option == "Display Hourly Averages":
    st.header("Display Hourly Averages")

    if uploaded_file is not None:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(uploaded_file)

        # Ensure the 'Timestamp' column is a datetime object
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])

        # Extract time-based features
        data['Hour'] = data['Timestamp'].dt.hour

        # Calculate hourly averages
        if all(col in data.columns for col in ['GHI', 'DNI', 'DHI', 'Tamb']):
            hourly_avg = data.groupby('Hour')[['GHI', 'DNI', 'DHI', 'Tamb']].mean()

            # Plotting hourly trends
            plt.figure(figsize=(14, 8))
            plt.subplot(2, 1, 2)
            hourly_avg.plot(ax=plt.gca(), colormap='coolwarm', alpha=0.8)
            plt.title("Hourly Averages of GHI, DNI, DHI, and Tamb")
            plt.ylabel("Values")
            plt.xlabel("Hour")
            plt.xticks(ticks=range(0, 24, 2))
            plt.legend(loc='upper left')

            # Display the plot
            st.pyplot(plt)
        else:
            st.warning("The CSV file is missing necessary columns: 'GHI', 'DNI', 'DHI', or 'Tamb'.")
    else:
        st.warning("Please Download a CSV file to view the hourly averages plot.")

# Option 4: Sensor Reading
elif selected_option == "Sensor Reading":
    st.header("Sensor Readings (Cleaned vs Not Cleaned)")

    if uploaded_file is not None:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(uploaded_file)

        # Ensure the 'Timestamp' column is a datetime object
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])

        # Check for the required columns
        if all(col in data.columns for col in ['ModA', 'ModB', 'Cleaning']):
            # Separate data into cleaned and not cleaned
            cleaned = data[data['Cleaning'] == 1]
            not_cleaned = data[data['Cleaning'] == 0]

            # Plot cleaned and not cleaned sensor readings
            plt.figure(figsize=(14, 8))

            # ModA - Cleaned and Not Cleaned
            plt.plot(cleaned['Timestamp'], cleaned['ModA'], label='ModA (Cleaned)', color='blue', alpha=0.7)
            plt.plot(not_cleaned['Timestamp'], not_cleaned['ModA'], label='ModA (Not Cleaned)', color='cyan', alpha=0.5)

            # ModB - Cleaned and Not Cleaned
            plt.plot(cleaned['Timestamp'], cleaned['ModB'], label='ModB (Cleaned)', color='green', alpha=0.7)
            plt.plot(not_cleaned['Timestamp'], not_cleaned['ModB'], label='ModB (Not Cleaned)', color='lime', alpha=0.5)

            # Add labels, title, and legend
            plt.title("Sensor Readings Over Time (Cleaned vs. Not Cleaned)")
            plt.xlabel("Time")
            plt.ylabel("Sensor Readings")
            plt.legend(loc='upper right', title='Legend')
            plt.tight_layout()

            # Display the plot
            st.pyplot(plt)
        else:
            st.warning("The CSV file is missing necessary columns: 'ModA', 'ModB', or 'Cleaning'.")
    else:
        st.warning("Please Download a CSV file to view the sensor readings plot.")

# Option 5: Correlation matrix for solar radiation and temperature
elif selected_option == "Correlation matrix for solar radiation and temperature":
    st.header("Correlation Matrix: Solar Radiation and Temperature")
    import seaborn as sns

    if uploaded_file is not None:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(uploaded_file)

        # Check if the necessary columns are present
        if all(col in data.columns for col in ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']):
            # Select relevant columns for solar radiation and temperature
            solar_temp_columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']

            # Calculate the correlation matrix for solar radiation and temperature
            solar_temp_corr = data[solar_temp_columns].corr()

            # Plot the correlation matrix as a heatmap
            plt.figure(figsize=(10, 6))
            sns.heatmap(solar_temp_corr, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
            plt.title('Correlation Matrix: Solar Radiation and Temperature')
            st.pyplot(plt)
        else:
            st.warning("The CSV file is missing necessary columns: 'GHI', 'DNI', 'DHI', 'TModA', or 'TModB'.")
    else:
        st.warning("Please Download a CSV file to view the correlation matrix.")
    
    # Option 6: Wind Direction Distribution
elif selected_option == "Wind Direction Distribution":
    st.header("Wind Direction Distribution")
    import seaborn as sns
    import numpy as np

    if uploaded_file is not None:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(uploaded_file)

        # Check if the necessary columns are present
        if all(col in data.columns for col in ['WD', 'WS']):
            # Extract relevant columns (wind direction, wind speed)
            wind_data = data[['WD', 'WS']].dropna()  # Remove NaN values

            # Set number of bins for wind direction (angles)
            direction_bins = np.arange(0, 360, 30)

            # Calculate the number of occurrences for each direction bin
            direction_hist, _ = np.histogram(wind_data['WD'], bins=direction_bins)

            # Set the bins for wind speed (optional)
            speed_bins = np.arange(0, 30, 5)  # For example, 0 to 30 m/s in 5 m/s intervals
            speed_hist, _ = np.histogram(wind_data['WS'], bins=speed_bins)

            # Plot wind rose-like plot for wind direction
            angles = np.linspace(0, 2 * np.pi, len(direction_hist), endpoint=False)
            angles = np.concatenate((angles, [angles[0]]))  # Close the circle
            direction_hist = np.concatenate((direction_hist, [direction_hist[0]]))  # Close the circle

            plt.figure(figsize=(8, 8))
            plt.subplot(111, polar=True)
            plt.bar(angles, direction_hist, width=0.3, color='blue', alpha=0.7)

            plt.title("Wind Direction Distribution")
            st.pyplot(plt)

        else:
            st.warning("The CSV file is missing necessary columns: 'WD' (Wind Direction) or 'WS' (Wind Speed).")
    else:
        st.warning("Please Download a CSV file to view the wind direction distribution.")

   # Option 7: Wind Speed Distribution
elif selected_option == "Wind Speed Distribution":
    st.header("Wind Speed Distribution")
    import seaborn as sns
    import numpy as np

    if uploaded_file is not None:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(uploaded_file)

        # Check if the necessary columns are present
        if 'WS' in data.columns:
            # Extract relevant column (wind speed)
            wind_speed_data = data['WS'].dropna()  # Remove NaN values

            # Set the bins for wind speed
            speed_bins = np.arange(0, 30, 5)  # For example, 0 to 30 m/s in 5 m/s intervals

            # Calculate the histogram for wind speed
            speed_hist, _ = np.histogram(wind_speed_data, bins=speed_bins)

            # Plot radial bar chart for wind speed distribution
            angles_speed = np.linspace(0, 2 * np.pi, len(speed_hist), endpoint=False)
            angles_speed = np.concatenate((angles_speed, [angles_speed[0]]))  # Close the circle
            speed_hist = np.concatenate((speed_hist, [speed_hist[0]]))  # Close the circle

            plt.figure(figsize=(8, 8))
            plt.subplot(111, polar=True)
            plt.bar(angles_speed, speed_hist, width=0.3, color='green', alpha=0.7)

            plt.title("Wind Speed Distribution (Radial Bar Plot)")
            st.pyplot(plt)

        else:
            st.warning("The CSV file is missing the necessary column: 'WS' (Wind Speed).")
    else:
        st.warning("Please Download a CSV file to view the wind speed distribution.")
        
        
