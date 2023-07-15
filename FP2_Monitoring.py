import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Reading dataset
monitoring_data = pd.read_csv("monitoring_data.csv")

# Calculating average MAPE
MAPE = round(monitoring_data['MAPE'].mean(), 4)
st.write("Average MAPE:", MAPE)

# Displaying monitoring data
st.write(monitoring_data[['ds', 'MAPE']].to_string(index=False))

# Plotting the line graph
st.line_chart(monitoring_data[['ds', 'MAPE']])

# Define threshold value
threshold = 0.05

# Plotting the threshold line
plt.axhline(y=threshold, color='r', linestyle='--', label='Threshold')
plt.xlabel('Month')
plt.ylabel('MAPE')
plt.title('MAPE with threshold 5%')

# Showing the plot
st.pyplot(plt)

# Calculate the average of all previous values
previous_avg = monitoring_data['y'].iloc[:-1].mean()

# Get the last value of the column
last_value = monitoring_data['y'].iloc[-1]

# Compare the last value with the average
if abs(last_value / previous_avg - 1) > 0.1:
    st.write("There is drift in actual data. Model might require retraining")
else:
    st.write("There is no drift in actual data. Model does not require retraining")

# Check if any value in the column is greater than 0.05
if (monitoring_data['MAPE'] > 0.05).any():
    st.write("MAPE is exceeding threshold, need to retrain model.")
else:
    st.write("MAPE is below threshold, no need to retrain model.")

# Reading CPI monitoring dataset
cpi_monitoring_data = pd.read_csv("cpi_Monitoring_data.csv")

# Calculating average MAPE
MAPE = round(cpi_monitoring_data['MAPE'].mean(), 4)
st.write("Average MAPE:", MAPE)

# Displaying CPI monitoring data
st.write(cpi_monitoring_data[['ds', 'MAPE']].to_string(index=False))

# Plotting the line graph for CPI
st.line_chart(cpi_monitoring_data[['ds', 'MAPE']])

# Plotting the threshold line for CPI
plt.axhline(y=threshold, color='r', linestyle='--', label='Threshold')
plt.xlabel('Month')
plt.ylabel('MAPE')
plt.title('MAPE with threshold 5%')

# Showing the plot for CPI
st.pyplot(plt)

# Calculate the average of all previous values for CPI
previous_avg = cpi_monitoring_data['CPIIN'].iloc[:-1].mean()

# Get the last value of the column for CPI
last_value = cpi_monitoring_data['CPIIN'].iloc[-1]

# Compare the last value with the average for CPI
if abs(last_value / previous_avg - 1) > 0.1:
    st.write("There is drift in actual data. Model might require retraining")
else:
    st.write("There is no drift in actual data. Model does not require retraining")

# Check if any value in the column is greater than 0.05 for CPI
if (cpi_monitoring_data['MAPE'] > 0.05).any():
    st.write("MAPE is exceeding threshold, need to retrain model.")
else:
    st.write("MAPE is below threshold, no need to retrain model.")
