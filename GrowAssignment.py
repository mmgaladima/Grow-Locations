import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Read in the dataset
df = pd.read_csv('GrowLocations.csv')

# Longitude and Latitude column swap
df['Longitude'], df['Latitude'] = df['Latitude'], df['Longitude']

# Remove rows not within Longitude and Latitude range
df = df[(df['Longitude'] >= -10.592) & (df['Longitude'] <= 1.6848) & 
        (df['Latitude'] >= 50.681) & (df['Latitude'] <= 57.985)]

# Remove duplicates based on Longitude and Latitude
df = df.drop_duplicates(subset=['Longitude', 'Latitude'])

# Read in the image
location_map = plt.imread('map7.png')

# Create a scatterplot with the map as the background
fig, ax = plt.subplots(figsize= (13,13))
ax.imshow(location_map, extent=[-10.592,1.6848,50.681,57.985])

# Plot the sensor locations on the map
ax.scatter(df['Longitude'], df['Latitude'], color='blue', s=35, label='locations')

# Title and labels of the plot 
plt.title('Sensor Locations on UK Map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Show legend
plt.legend()

# Show plot
plt.show()

# Save the cleaned DataFrame to a new CSV file
df.to_csv('GrowLocations_clean.csv', index=False)