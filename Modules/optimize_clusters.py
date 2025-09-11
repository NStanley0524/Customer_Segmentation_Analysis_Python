import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from Modules.data_upload import st

# This module plots the elbow method to determine the optimal cluster for the clustering technique

def plot_elbow_method(df,selected_features):
    if df is not None and selected_features:
        wcss = []
        for i in range(2,11):
            kmeans = KMeans(n_clusters=i,random_state=42) # Initiate KMeans clustering
            kmeans.fit(df[selected_features]) # Apply clustering
            wcss.append(kmeans.inertia_) # Get the inertia

        # Plotting the elbow method
        fig,ax = plt.subplots(figsize =(8,6))
        ax.plot(range(2,11),wcss,marker="o",color = "b")
        ax.set_title("Elbow Method for Optimal Clusters")
        ax.set_ylabel("Inertia")
        ax.set_xlabel("Number of Clusters")
        st.pyplot(fig)


        optimal_clusters = st.sidebar.slider("Optimal Number of Clusters",2,10,3)
        return optimal_clusters
    return 3

