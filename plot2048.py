import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
df = pd.read_csv('plots/copper, nickel, brass, 2048, g=-4.csv')

# Split the data into three parts
copper_data = df.iloc[0:2048].copy()
zinc_data = df.iloc[2049:4098].copy()
brass_data = df.iloc[4098:6147].copy()

# Save the split data into separate CSV files
copper_data.to_csv('plots/copper_data2048.csv', index=False)
zinc_data.to_csv('plots/zinc_data2048.csv', index=False)
brass_data.to_csv('plots/brass_data2048.csv', index=False)

# Load the separate CSV files
#copper_data = pd.read_csv('plots/copper_data2048.csv', skiprows=2, skipfooter=1, usecols=(1, 3))
zinc_data = pd.read_csv('plots/zinc_data2048.csv')
brass_data = pd.read_csv('plots/brass_data2048.csv')
copper_data = np.loadtxt('plots/copper_data2048.csv', delimiter=',', skiprows=1, usecols=(1, 3))

print(copper_data)
copper_energy = copper_data[::,1]
copper_freq = copper_data[::,0]
print(copper_freq)
plt.plot(copper_energy, copper_freq)
plt.show()
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
plt.plot(copper_data['Events N'], label='Copper', color='blue')
plt.plot(zinc_data['Events N'], label='Zinc', color='red')
plt.plot(brass_data['Events N'], label='Brass', color='black')

# Add labels and title
plt.xlabel('Energy (keV)')
plt.ylabel('Frequency')
plt.title('Energy Distribution of Copper, Zinc, and a Brass Candidate')

# Show legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
