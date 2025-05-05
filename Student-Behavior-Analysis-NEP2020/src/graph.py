import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (update the path if needed)
data = pd.read_excel('C:\\Users\\lucky\\OneDrive\\Desktop\\Association Rule\\BA_student.xlsx')

# Check the first few rows to confirm data structure (optional)
print(data.head())

# Generate a bar graph for the Q5 column
plt.figure(figsize=(10, 6))
data['division'].value_counts().plot(kind='bar', color='green')

# Adding titles and labels
plt.title('Bar Graph of division', fontsize=16)
plt.xlabel('division Categories', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Display the plot
plt.show()