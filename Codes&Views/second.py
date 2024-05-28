import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('dataset.csv')

# Filter the dataset for benign and potentially malicious traffic
benign_traffic = df[df['Label'] == 'Benign']
malicious_traffic = df[df['Label'] != 'Benign']

# Calculate flag counts for benign traffic
benign_syn_count = benign_traffic['SYN Flag Cnt'].sum()
benign_rst_count = benign_traffic['RST Flag Cnt'].sum()
benign_fin_count = benign_traffic['FIN Flag Cnt'].sum()

# Calculate flag counts for malicious traffic
malicious_syn_count = malicious_traffic['SYN Flag Cnt'].sum()
malicious_rst_count = malicious_traffic['RST Flag Cnt'].sum()
malicious_fin_count = malicious_traffic['FIN Flag Cnt'].sum()

# Create a bar plot
labels = ['SYN', 'RST', 'FIN']
benign_counts = [benign_syn_count, benign_rst_count, benign_fin_count]
malicious_counts = [malicious_syn_count, malicious_rst_count, malicious_fin_count]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, benign_counts, width, label='Benign')
rects2 = ax.bar(x + width/2, malicious_counts, width, label='Malicious')

ax.set_ylabel('Flag Count')
ax.set_title('Flag Counts for Benign and Malicious Traffic')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()
