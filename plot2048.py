import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('plots/copper, nickel, brass, 2048, g=-4.csv')

# Split the data into three parts
copper_data = df.iloc[0:2049].copy()
zinc_data = df.iloc[2049:4098].copy()
brass_data = df.iloc[4098:6147].copy()

# Save the split data into separate CSV files
copper_data.to_csv('plots/copper_data2048.csv', index=False)
zinc_data.to_csv('plots/zinc_data2048.csv', index=False)
brass_data.to_csv('plots/brass_data2048.csv', index=False)

# Load the separate CSV files
copper_data = pd.read_csv('plots/copper_data2048.csv')
zinc_data = pd.read_csv('plots/zinc_data2048.csv')
brass_data = pd.read_csv('plots/brass_data2048.csv')

# Convert 'Events N' to numeric
copper_data['Events N'] = pd.to_numeric(copper_data['Events N'], errors='coerce')
zinc_data['Events N'] = pd.to_numeric(zinc_data['Events N'], errors='coerce')
brass_data['Events N'] = pd.to_numeric(brass_data['Events N'], errors='coerce')

# Drop NaN values
copper_data.dropna(subset=['Events N'], inplace=True)
zinc_data.dropna(subset=['Events N'], inplace=True)
brass_data.dropna(subset=['Events N'], inplace=True)

# Create a plot
plt.figure(figsize=(10, 6))

# Plot frequency line graphs
plt.plot(copper_data['Events N'], label='Copper', color='orange')
plt.plot(zinc_data['Events N'], label='Zinc', color='blue')
plt.plot(brass_data['Events N'], label='Brass', color='green')

# Add labels and title
plt.xlabel('Events N')
plt.ylabel('Frequency')
plt.title('Frequency Distribution of Events N for Copper, Zinc, and Brass')

# Show legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
