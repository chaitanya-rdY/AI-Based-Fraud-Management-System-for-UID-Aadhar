import pandas as pd

# Example dataframes for demonstration
new_data = pd.DataFrame({
    'ID': [1, 2, 3],
    'Value': ['A', 'B', 'C']
})

existing_data = pd.DataFrame({
    'ID': [1, 2, 4],
    'Value': ['X', 'Y', 'Z']
})

# Set 'ID' as the index for both dataframes
new_data.set_index('ID', inplace=True)
existing_data.set_index('ID', inplace=True)

# Combine new_data with existing_data
combined_data = new_data.combine_first(existing_data)

# Reset index if needed
combined_data.reset_index(inplace=True)

print(combined_data)
