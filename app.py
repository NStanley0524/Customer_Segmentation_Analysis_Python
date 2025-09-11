import streamlit as st
from Modules.data_upload import upload_data
from Modules.feature_selection import select_features
from Modules.optimize_clusters import plot_elbow_method
from Modules.kmeans_clustering import perform_clustering
from Modules.pca_plot import plot_pca
from Modules.cluster_summary import display_cluster_summary
from Modules.data_download import download_clustered_data


def main():
    df,uploaded_data = upload_data()


    if df is not None:
        selected_features  = select_features(df)


        if selected_features and len(selected_features) > 0 :
            optimal_clusters = plot_elbow_method(df,selected_features)



            labels , kmeans, scaled_data = perform_clustering(df,selected_features,optimal_clusters)



            # Check if clustering was successful
            if scaled_data is not None and labels is not None and len(labels)>0:
                plot_pca(df,selected_features,labels,scaled_data)



                display_cluster_summary(df,labels)



                download_clustered_data(df,labels)
            else:
                st.error("Clustering faild. Please check your data and try again")

        else:
            st.warning("Please select at least one feature for clustering")


if __name__ == "__main__":
    main()