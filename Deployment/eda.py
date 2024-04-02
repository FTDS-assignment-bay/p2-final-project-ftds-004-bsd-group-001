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

if __name__ == '__main__':
    run()
