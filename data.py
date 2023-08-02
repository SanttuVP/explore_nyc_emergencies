import pandas as pd

# Step 2: Read the original CSV file
original_file = "nyc_311.csv"
df = pd.read_csv(original_file)

# Step 3: Create a new DataFrame with only the desired columns
selected_columns = ["Unique Key", "Complaint Type", "Created Date", "Borough", "Longitude", "Latitude"]
new_df = df[selected_columns]

# Step 4: Save the new DataFrame to a new CSV file
new_csv_file = "nyc_311_selected_columns.csv"
new_df.to_csv(new_csv_file, index=False)
