import streamlit as st
from Modules.data_upload import upload_data

# This Module lets you select the features for clustering

def select_features(df):
    if df is not None:
        numerical_cols = df.select_dtypes(include=[float,int]).columns.tolist() # Get the numerical columns of the dataset
        selected_features = st.sidebar.multiselect(
            "Select features for clustering",numerical_cols,default=numerical_cols
        ) # Put the numerical columns to the streamlit sidebar for users to select from

        if len(selected_features) == 0: # If no numerical column is present in data
            st.warning("Data contains no numerical column or no Feature selected. Please select a feature for clustering")

        st.write("Selected features for clustering:")
        st.write(selected_features)
        return selected_features
    return[]
