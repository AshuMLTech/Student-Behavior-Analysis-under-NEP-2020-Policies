import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Load the binary encoded dataset
data = pd.read_csv('Student-Behavior-Analysis-NEP2020\data\processed\BA_Student (modify).xlsx')

# Step 2: Apply the Apriori algorithm to find frequent itemsets
# Set min_support according to your analysis needs
min_support = 0.1  # Example: change as necessary
frequent_itemsets = apriori(data, min_support=min_support, use_colnames=True)

# Step 3: Generate association rules
# Set min_threshold according to your analysis needs
min_threshold = 0.5  # Example: change as necessary
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_threshold)

# Step 4: Save the association rules to a CSV file
output_path = ('Student-Behavior-Analysis-NEP2020\results')
rules.to_csv(output_path, index=False)

# Step 5: Print the rules and confirm saving
print(f"Association rules have been generated and saved to '{output_path}'")
print(rules)
