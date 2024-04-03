import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Add CSS style for color theme
st.markdown(
    """
    <style>
    /* Set text color */
    body {
        color: #333333;
    }

    /* Set background color */
    .stApp {
        background-color: #659DBd;
    }
    .divider {
        background-color: #000000; /* Black color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def run():
    st.markdown('<h1 style="text-align: center; color: white;">APART HELPER EDA</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;">Apart Helper is a product website designed to assist customers in choosing apartments or properties based on their preferences.</p>', unsafe_allow_html=True)
    st.divider()

    # Melakukan loading dataset
    data_sebelum = pd.read_csv('properties_data.csv')
    data_sesudah = pd.read_csv('data_setelah_clustering.csv', index_col=0)

    st.header('Exploratory Data Analysis Sebelum Cluster', divider='rainbow')
    st.subheader('Top 5 Location By Average Price')

    # Calculate the average price for each neighborhood
    avg_price_by_neighborhood = data_sebelum.groupby('neighborhood')['price'].mean()

    # Sort the average prices in descending order and select the top 5
    top_5_avg_price = avg_price_by_neighborhood.sort_values(ascending=False).head(5)

    # Display the top 5 neighborhoods using Streamlit
    st.bar_chart(top_5_avg_price)

    st.subheader('Number of Bedrooms',divider='rainbow')

    



if __name__ == '__main__':
    run()
