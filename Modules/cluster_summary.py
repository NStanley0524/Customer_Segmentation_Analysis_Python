import streamlit as st


def display_cluster_summary(df,labels):
    if df is not None and labels is not None and len(labels)>0:
        df_copy = df.copy() # Create a copy to avoid modifying the original
        df_copy["Cluster"] = labels

        # Only calculate mean for numeric columns
        numeric_col = df_copy.select_dtypes(include = ["number"]).columns

        if len(numeric_col) > 0:
            cluster_summary = df_copy.groupby("Cluster")[numeric_col].mean()
            st.write("Cluster Summary (Mean of Features in each Cluster):")
            st.write(cluster_summary)

            #  Also Show cluster counts
            cluster_counts = df_copy["Cluster"].value_counts().sort_index()
            st.write("Cluster sizes")
            st.write(cluster_counts)

        else:
            st.warning("No numeric columns founds for cluster summary")

            # Still show cluster counts
             
            cluster_counts = df_copy["Cluster"].value_counts().sort_index()
            st.write("Cluster sizes")
            st.write(cluster_counts)



