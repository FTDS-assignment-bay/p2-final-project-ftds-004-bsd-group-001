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

    # Group data by 'no_of_bathrooms' and count frequencies
    bathroom_counts = data_sebelum['no_of_bedrooms'].value_counts().sort_index()

    # Plot bar chart using Streamlit
    st.bar_chart(bathroom_counts)

    st.subheader('Number of Bathrooms',divider='rainbow')

    # Group data by 'no_of_bathrooms' and count frequencies
    bathroom_counts = data_sebelum['no_of_bathrooms'].value_counts().sort_index()

    # Plot bar chart using Streamlit
    st.bar_chart(bathroom_counts)


    st.header('Exploratory Data Analysis Setelah Cluster', divider='rainbow')
    # Assuming mean_data is your DataFrame containing the mean prices for each cluster
    mean_data = data_sesudah.groupby('cluster')['price'].mean().reset_index()
    mean_data['cluster'] = mean_data['cluster'].astype(int)  # Ensure 'cluster' column is of integer type
    mean_data = mean_data.round(0).astype(int)

    # Display the DataFrame in Streamlit
    st.dataframe(mean_data)

    st.subheader('Average Price by Cluste',divider='rainbow')

    # Assuming mean_data is your DataFrame containing the mean prices for each cluster
    mean_data = data_sesudah.groupby('cluster')['price'].mean().reset_index()
    mean_data['cluster'] = mean_data['cluster'].astype(int)  # Ensure 'cluster' column is of integer type
    mean_data = mean_data.round(0).astype(int)

    # Plot stacked bar chart
    st.bar_chart(mean_data.set_index('cluster'), use_container_width=True)

    st.subheader('Top 5 Location By Average Price Based on Price',divider='rainbow')
    # Filter data for the top 5 neighborhoods
    top_5_avg_price = avg_price_by_neighborhood.sort_values(ascending=False).head(5)
    filtered_data = data_sesudah[data_sesudah['neighborhood'].isin(top_5_avg_price.index)]

    # Group by 'neighborhood' and 'cluster', then calculate the average price for each group
    avg_price_by_neighborhood_cluster = filtered_data.groupby(['neighborhood', 'cluster'])['price'].mean().unstack()

    # Plot stacked bar chart for top 5 neighborhoods
    st.bar_chart(avg_price_by_neighborhood_cluster, use_container_width=True)    


    st.subheader('Number of Bedrooms Based on Cluster',divider='rainbow')
    # Group data by 'no_of_bathrooms' and 'cluster', then count frequencies
    bathroom_cluster_counts = data_sesudah.groupby(['no_of_bedrooms', 'cluster']).size().unstack(fill_value=0)

    # Plot stacked bar chart
    st.bar_chart(bathroom_cluster_counts, use_container_width=True)

    st.subheader('Number of Bathrooms Based on Cluster',divider='rainbow')
    # Group data by 'no_of_bathrooms' and 'cluster', then count frequencies
    bathroom_cluster_counts = data_sesudah.groupby(['no_of_bathrooms', 'cluster']).size().unstack(fill_value=0)

    # Plot stacked bar chart
    st.bar_chart(bathroom_cluster_counts, use_container_width=True)

if __name__ == '__main__':
    run()
