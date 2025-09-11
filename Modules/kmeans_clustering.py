import streamlit as st

from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler



def perform_clustering(df,selected_features,optimal_clusters):
    if df is not None and selected_features:

        scaler = StandardScaler() # Initialize scaling
        scaled_data = scaler.fit_transform(df[selected_features]) # Scaling the selected features


        # Performing  validation

        if len(scaled_data.shape) != 2 or scaled_data.shape[1] < 2: # If scaled data is not 2D
            st.write("Error : Scaled data is not 2D or has more than 2 Features")
            return [],None,None
        
        if len(scaled_data.shape) == 1: # If scaled data is 1D, reshape to 2D
            scaled_data = scaled_data.reshape(-1,1)

        
        # Performing clustering for scaled data that is 2D
        
        try:
            kmeans = KMeans(n_clusters=optimal_clusters,random_state=42,n_init=10)
            labels = kmeans.fit_predict(scaled_data)

            st.write(f"Unique Clusters : {len(set(labels))}")

            # Calculate silhuotte score only if we have more than 1 cluster
            if len(set(labels)) > 1:
                sil_score = silhouette_score(scaled_data,labels)
                st.write(f"Silhuoette Score {sil_score:.3f}")
            else:
                st.warning("Only One cluster found...Silhuoette score not applicable")

            return labels,kmeans,scaled_data
        
        except Exception as e:
            st.error(f"Clustering failed : {str(e)}")
            return [], None,None
        
    return [], None,None


