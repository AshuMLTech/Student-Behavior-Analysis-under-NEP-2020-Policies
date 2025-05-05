import pandas as pd
import matplotlib.pyplot as plt

# Replace with the actual file path where your CSV is located
data = pd.read_excel('C:\\Users\\lucky\\OneDrive\\Desktop\\Association Rule\\BA_student.xlsx')

# Check the first few rows to understand the data (optional)
print(data.head())

# Plot a bar graph for Q4 column
plt.figure(figsize=(10, 6))
data['community'].value_counts().plot(kind='bar', color='red')

# Adding titles and labels
plt.title('Bar Graph of community', fontsize=16)
plt.xlabel('community Center', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Display the plot
plt.show()