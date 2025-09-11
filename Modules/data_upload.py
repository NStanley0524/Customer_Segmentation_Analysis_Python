import streamlit as st
import pandas as pd

# This module enables user to upload the file they need for clustering

def upload_data():
    st.title("Customer Segmentation Analysis")
    uploaded_file = st.file_uploader("Upload a CSV file",type=["csv"],key="csv_uploader_data_upload")


    if uploaded_file is not None: # If Data contains a file
        df = pd.read_csv(uploaded_file) # Read the file
        st.write(f"Dataset Preview:")
        st.write(df.head()) # Print the first 5 rows of the data
        return df,uploaded_file
    
    else:
        return None,uploaded_file

