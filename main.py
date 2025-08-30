import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# ==================== Step 1: Load Dataset ====================
data = pd.read_csv('student-mat.csv', delimiter=';')

# Only numeric columns
numeric_data = data.select_dtypes(include='number')

# ==================== Step 2: Summary Statistics ====================
summary = []
for col in numeric_data.columns:
    min_val = numeric_data[col].min()
    max_val = numeric_data[col].max()
    q1 = numeric_data[col].quantile(0.25)
    q3 = numeric_data[col].quantile(0.75)
    iqr = q3 - q1
    summary.append({
        'Column': col,
        'Min': min_val,
        'Max': max_val,
        'Q1': q1,
        'Q3': q3,
        'IQR': iqr
    })
summary_df = pd.DataFrame(summary)

# ==================== Step 3: Clustering ====================
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_data)

# KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(scaled_data)

# DBSCAN
dbscan = DBSCAN(eps=2, min_samples=5)
dbscan_labels = dbscan.fit_predict(scaled_data)

# ==================== Step 4: PCA for Visualization ====================
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)

plt.figure()
plt.scatter(pca_data[:, 0], pca_data[:, 1], c=kmeans_labels, cmap='viridis', s=30)
plt.title('KMeans Clustering (PCA Projection)')
plt.savefig('kmeans_plot.png')

plt.figure()
plt.scatter(pca_data[:, 0], pca_data[:, 1], c=dbscan_labels, cmap='plasma', s=30)
plt.title('DBSCAN Clustering (PCA Projection)')
plt.savefig('dbscan_plot.png')

# ==================== Step 5: Export Report to PDF ====================
doc = SimpleDocTemplate("report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
flow = []

flow.append(Paragraph("Student Dataset Analysis Report", styles['Title']))
flow.append(Spacer(1, 20))

flow.append(Paragraph("Summary Statistics", styles['Heading2']))
flow.append(Paragraph(summary_df.to_html(index=False), styles['Normal']))
flow.append(Spacer(1, 20))

flow.append(Paragraph("KMeans Clustering (3 clusters)", styles['Heading2']))
flow.append(Image('kmeans_plot.png', width=400, height=300))
flow.append(Spacer(1, 20))

flow.append(Paragraph("DBSCAN Clustering", styles['Heading2']))
flow.append(Image('dbscan_plot.png', width=400, height=300))

doc.build(flow)
print("Analysis complete. Report saved as report.pdf")