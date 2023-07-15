import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Reading dataset
monitoring_data = pd.read_csv("monitoring_data.csv")

# Calculating average MAPE
MAPE = round(monitoring_data['MAPE'].mean(), 4)
st.write("Average MAPE:", MAPE)

# # Displaying monitoring data
# st.write(monitoring_data[['ds', 'MAPE']].to_string(index=False))

# Plotting the line graph
fig, ax = plt.subplots()
ax.plot(monitoring_data['ds'], monitoring_data['MAPE'])
ax.axhline(y=0.05, color='r', linestyle='--', label='Threshold')
ax.set_xlabel('Month')
ax.set_ylabel('MAPE')
ax.set_title('MAPE with threshold 5%')
ax.legend()

# Showing the plot
st.pyplot(fig)

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

# # Displaying CPI monitoring data
# st.write(cpi_monitoring_data[['ds', 'MAPE']].to_string(index=False))

# Plotting the line graph for CPI
fig_cpi, ax_cpi = plt.subplots()
ax_cpi.plot(cpi_monitoring_data['ds'], cpi_monitoring_data['MAPE'])
ax_cpi.axhline(y=0.05, color='r', linestyle='--', label='Threshold')
ax_cpi.set_xlabel('Month')
ax_cpi.set_ylabel('MAPE')
ax_cpi.set_title('MAPE with threshold 5%')
ax_cpi.legend()

# Showing the plot for CPI
st.pyplot(fig_cpi)

# Calculate the average of all previous values for CPI
previous_avg_cpi = cpi_monitoring_data['CPIIN'].iloc[:-1].mean()

# Get the last value of the column for CPI
last_value_cpi = cpi_monitoring_data['CPIIN'].iloc[-1]

# Compare the last value with the average for CPI
if abs(last_value_cpi / previous_avg_cpi - 1) > 0.1:
    st.write("There is drift in actual data. Model might require retraining")
else:
    st.write("There is no drift in actual data. Model does not require retraining")

# Check if any value in the column is greater than 0.05 for CPI
if (cpi_monitoring_data['MAPE'] > 0.05).any():
    st.write("MAPE is exceeding threshold, need to retrain model.")
else:
    st.write("MAPE is below threshold, no need to retrain model.")
