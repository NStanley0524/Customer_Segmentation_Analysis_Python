import streamlit as st



def download_clustered_data(df,labels):
    if df is not None and labels is not None and len(labels) >0:
        df_copy = df.copy() # Avoid modifying original
        df_copy["Clusters"] = labels


        def convert_df(df):
            return df.to_csv(index=False).encode("utf-8") # Convert to csv format
        


        csv = convert_df(df)
        st.download_button(
            label="Download Clustered Data",
            data=csv,
            file_name="Clustered Data.csv",
            mime="text/csv"
            )
        

