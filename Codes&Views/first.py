import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('dataset.csv')

# Filter the dataset for benign and potentially malicious traffic
benign_traffic = df[df['Label'] == 'Benign']
malicious_traffic = df[df['Label'] != 'Benign']

# Calculate average packet lengths for benign traffic
benign_avg_fwd_pkt_len = benign_traffic['Fwd Pkt Len Mean'].mean()
benign_avg_bwd_pkt_len = benign_traffic['Bwd Pkt Len Mean'].mean()

# Calculate average packet lengths for malicious traffic
malicious_avg_fwd_pkt_len = malicious_traffic['Fwd Pkt Len Mean'].mean()
malicious_avg_bwd_pkt_len = malicious_traffic['Bwd Pkt Len Mean'].mean()

# Create a bar plot
labels = ['Benign Forward', 'Benign Backward', 'Malicious Forward', 'Malicious Backward']
avg_lengths = [benign_avg_fwd_pkt_len, benign_avg_bwd_pkt_len, malicious_avg_fwd_pkt_len, malicious_avg_bwd_pkt_len]

plt.bar(labels, avg_lengths, color=['blue', 'blue', 'red', 'red'])
plt.ylabel('Average Packet Length')
plt.title('Average Packet Lengths for Benign and Malicious Traffic')
plt.xticks(rotation=45, ha='right')
plt.show()
