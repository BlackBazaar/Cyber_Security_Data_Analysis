import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("dataset.csv")

# Filter benign and malicious traffic
benign_traffic = df[df['Label'] == 'Benign']
malicious_traffic = df[df['Label'] != 'Benign']

# Define the flow features to analyze
flow_features = ['Flow Duration', 'Flow Byts/s', 'Flow Pkts/s', 'Flow IAT Mean', 'Flow IAT Std']

# Plot the comparison
plt.figure(figsize=(15, 10))

for i, feature in enumerate(flow_features, start=1):
    plt.subplot(2, 3, i)
    
    # Filter out infinite or NaN values
    benign_values = benign_traffic[feature].replace([np.inf, -np.inf], np.nan).dropna()
    malicious_values = malicious_traffic[feature].replace([np.inf, -np.inf], np.nan).dropna()
    
    # Adjust the range of histogram bins
    max_value = max(benign_values.max(), malicious_values.max())
    bins = np.linspace(0, max_value, 30)
    
    # Plot histograms
    plt.hist(benign_values, bins=bins, alpha=0.5, color='blue', label='Benign', density=True)
    plt.hist(malicious_values, bins=bins, alpha=0.5, color='red', label='Malicious', density=True)
    plt.title(feature)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()

plt.tight_layout()
plt.show()
