import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
@st.cache_data
def load_data():
    line_data = pd.read_csv('csv/Line_Chart_Data.csv')
    bar_data = pd.read_csv('csv/Bar_Chart_Data.csv')
    pie_data = pd.read_csv('csv/Pie_Chart_Data.csv')
    return line_data, bar_data, pie_data

line_data, bar_data, pie_data = load_data()

# Page title
st.title("Weather Data Visualization")

# Line chart visualization
st.subheader("Temperature Trends (Line Chart)")
for city in ['Riyadh', 'Jeddah', 'Mecca', 'Medina', 'Dammam']:
    st.write(f"### {city}")
    st.line_chart(line_data[['Date', f'{city}_High', f'{city}_Low']].set_index('Date'))

# Bar chart visualization
st.subheader("Average Wind Speed (Bar Chart)")
fig, ax = plt.subplots()
ax.bar(bar_data['City'], bar_data['Average_Wind_Speed_km_h'])
st.pyplot(fig)

# Pie chart visualization
st.subheader("Weather Conditions (Pie Chart)")
for index, row in pie_data.iterrows():
    st.write(f"### {row['City']}")
    labels = ['Clear', 'Overcast', 'Partly Cloudy']
    sizes = [row['Clear'], row['Overcast'], row['Partly_Cloudy']]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax1.axis('equal')
    st.pyplot(fig1)