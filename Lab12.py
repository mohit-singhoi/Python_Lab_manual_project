#Q.12 Use visualization techniques (scatter plot) to explore dataset patterns.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'Area': [1000, 1200, 1500, 1800, 2000],
    'Price': [150, 180, 220, 270, 300],
    'Bedrooms': [2, 2, 3, 4, 4]
}
df = pd.DataFrame(data)

# Scatter plot with hue for Bedrooms
sns.scatterplot(x='Area', y='Price', hue='Bedrooms', palette='viridis', s=100, data=df)
plt.title('Scatter Plot: Area vs Price (Colored by Bedrooms)')
plt.xlabel('Area (sqft)')
plt.ylabel('Price ($1000s)')
plt.legend(title='Bedrooms')
plt.show()
# Box plot for Price by Bedrooms
