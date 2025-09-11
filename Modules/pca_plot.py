import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


def plot_pca(df, selected_features, labels, scaled_data):  
    if df is not None and len(selected_features) > 0 and labels is not None and len(labels) > 0:
        

        # Handle 1D case
        if len(scaled_data.shape) == 1:
            scaled_data = scaled_data.reshape(-1, 1)
        
        # Check if we have enough features for PCA
        if scaled_data.shape[1] < 2:
            st.warning("PCA requires at least 2 features...reducing to 1D")
            pca = PCA(n_components=1)
            pca_components = pca.fit_transform(scaled_data)
            df_pca = pd.DataFrame(pca_components, columns=["PCA1"])
        else:
            pca = PCA(n_components=2)
            pca_components = pca.fit_transform(scaled_data)
            df_pca = pd.DataFrame(pca_components, columns=["PCA1", "PCA2"])

        # Check for length mismatch
        if len(labels) != len(df_pca):
            st.error(f"Mismatch in the number of labels ({len(labels)}) and PCA components ({len(df_pca)})")
            return

        df_pca["Cluster"] = labels

        # Create the plot
        fig, ax = plt.subplots(figsize=(8, 6))
        
        if df_pca.shape[1] >= 3:  # We have PCA1, PCA2, and Cluster columns
            # 2D scatter plot
            scatter = ax.scatter(df_pca['PCA1'], df_pca["PCA2"], c=df_pca["Cluster"], s=100, cmap="viridis")
            ax.set_ylabel("Principal Component 2")
            ax.set_xlabel("Principal Component 1")
        else:  # Only PCA1 and Cluster columns (1D case)
            # 1D scatter plot
            scatter = ax.scatter(df_pca['PCA1'], np.zeros_like(df_pca["PCA1"]), c=df_pca["Cluster"], s=100, cmap="viridis")
            ax.set_ylabel("")
            ax.set_xlabel("Principal Component 1")

        ax.set_title("PCA - KMeans Clusters")
        
        # Add colorbar
        plt.colorbar(scatter, ax=ax, label='Cluster')
        
        st.pyplot(fig)
