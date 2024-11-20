# from sklearn.manifold import TSNE
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import seaborn as sn
# from sklearn import preprocessing

# bw = pd.read_csv("./data/bw.csv")
# # `bw` contains your data
# Train_data = bw

# # Encode categorical features
# le = preprocessing.LabelEncoder()
# for column_name in Train_data.columns:
#     if Train_data[column_name].dtype == object:
#         Train_data[column_name] = le.fit_transform(Train_data[column_name])

# # Initialize t-SNE model
# model = TSNE(n_components=2, random_state=0, perplexity=100, learning_rate=500)

# # Fit and transform the data
# tsne_data = model.fit_transform(Train_data)

# # Create a DataFrame for visualization
# tsne_df = pd.DataFrame(data=tsne_data, columns=["Dim_1", "Dim_2"])

# # Here, we'll create random labels as an example:
# np.random.seed(0)
# tsne_df["label"] = np.random.randint(0, 5, size=tsne_df.shape[0])

# # Plot the t-SNE results in 2D with color coding
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111)

# # Create a colormap
# palette = sn.color_palette("hsv", n_colors=len(tsne_df["label"].unique()))

# # Scatter plot with color coding
# sc = ax.scatter(
#     tsne_df["Dim_1"], tsne_df["Dim_2"],
#     c=tsne_df["label"], cmap=plt.cm.get_cmap('YlOrRd', len(palette)), s=50, alpha=0.7
# )

# # Add a colorbar
# cb = plt.colorbar(sc, ax=ax, pad=0.1)
# cb.set_label("Label Categories", fontsize=12)

# # Set titles and labels
# ax.set_title("t-SNE Visualization", fontsize=16)
# ax.set_xlabel("Dimension 1", fontsize=12)
# ax.set_ylabel("Dimension 2", fontsize=12)
# plt.show()
import streamlit as st
st.image("./data/2_Dimentional_reduction_PreImputation.JPG", caption="Dimensionality reduction 2D")

# from sklearn.manifold import TSNE
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import seaborn as sn
# from sklearn import preprocessing

# # Assuming `bw` contains your data
# train_data_Sex = pd.DataFrame(bw["SEX"])

# # Encode categorical features
# le = preprocessing.LabelEncoder()
# for column_name in train_data_Sex.columns:
#     if train_data_Sex[column_name].dtype == object:
#         train_data_Sex[column_name] = le.fit_transform(train_data_Sex[column_name])

# # Initialize t-SNE model
# model = TSNE(n_components=2, random_state=0, perplexity=100, learning_rate=500)

# # Fit and transform the data
# tsne_data = model.fit_transform(train_data_Sex)

# # Create a DataFrame for visualization
# tsne_df = pd.DataFrame(data=tsne_data, columns=["Dim_1", "Dim_2"])

# # Here, we'll create random labels as an example:
# np.random.seed(0)
# tsne_df["label"] = np.random.randint(0, 5, size=tsne_df.shape[0])  # Replace with real labels

# # Plot the t-SNE results in 3D with color coding
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111)

# # Create a colormap
# palette = sn.color_palette("hsv", n_colors=len(tsne_df["label"].unique()))

# # Scatter plot with color coding
# sc = ax.scatter(
#     tsne_df["Dim_1"], tsne_df["Dim_2"],
#     c=tsne_df["label"], cmap=plt.cm.get_cmap('YlOrRd', len(palette)), s=50, alpha=0.7
# )

# # Add a colorbar
# cb = plt.colorbar(sc, ax=ax, pad=0.1)
# cb.set_label("Label Categories", fontsize=12)

# # Set titles and labels
# ax.set_title("t-SNE Visualization (2D, Colored by Label)", fontsize=16)
# ax.set_xlabel("Dimension 1", fontsize=12)
# ax.set_ylabel("Dimension 2", fontsize=12)
# #ax.set_zlabel("Dimension 3", fontsize=12)
# plt.show()

st.image("./data/Gender_2D.JPG", caption="Gender_into_2D")
