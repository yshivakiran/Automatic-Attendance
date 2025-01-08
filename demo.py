# import os
# import pandas as pd

# # Specify the folder containing the CSV files
# folder_path = r"C:\Users\91756\Desktop\FaceRec-Attendance\FaceRec-Attendance\Attendance"

# # Specify the category column to count
# category_column = "Enrollment"  # Change to the actual column name

# # Initialize an empty DataFrame to hold merged data
# merged_data = pd.DataFrame()

# # Iterate through all CSV files in the folder
# for filename in os.listdir(folder_path):
#     if filename.endswith(".csv"):
#         file_path = os.path.join(folder_path, filename)
#         # Read each CSV file and append it to the merged_data DataFrame
#         data = pd.read_csv(file_path)
#         merged_data = pd.concat([merged_data, data], ignore_index=True)

# # Count the occurrences of each category
# category_counts = merged_data[category_column].value_counts()

# # Save the merged data to a new CSV file
# merged_data.to_csv("merged_data.csv", index=False)

# # Save the category counts to a separate CSV file
# category_counts.to_csv("category_counts.csv", header=["Count"])

# print("Merging complete. Files 'merged_data.csv' and 'category_counts.csv' have been created.")


import os
import pandas as pd

# Specify the folder containing the CSV files
folder_path = r"C:\Users\91756\Desktop\FaceRec-Attendance\FaceRec-Attendance\Attendance"

# Specify the prefix to match
file_prefix = "java_"

# Specify the column to count
category_column = "Enrollment"  # Change to the actual column name

# Initialize an empty DataFrame to hold merged data
merged_data = pd.DataFrame()

# Find and process files that match the prefix
file_count = 0
for filename in os.listdir(folder_path):
    if filename.startswith(file_prefix) and filename.endswith(".csv"):
        file_count += 1
        file_path = os.path.join(folder_path, filename)
        # Read each matching CSV file and append it to the merged_data DataFrame
        data = pd.read_csv(file_path)
        merged_data = pd.concat([merged_data, data], ignore_index=True)

# Count the occurrences of each category
if not merged_data.empty:
    category_counts = merged_data[category_column].value_counts()

    # Save the merged data to a new CSV file
    merged_data.to_csv(f"{file_prefix}_merged.csv", index=False)

    # Save the category counts to a separate CSV file
    category_counts.to_csv(f"C:\Users\91756\Desktop\FaceRec-Attendance\FaceRec-Attendance\Attendance\count\{file_prefix}_category_counts.csv", header=["Count"])

    print(f"Merging complete. {file_count} files matched the prefix '{file_prefix}'.")
    print(f"Files '{file_prefix}_merged.csv' and '{file_prefix}_category_counts.csv' have been created.")
else:
    print(f"No files with prefix '{file_prefix}' found in the folder.")
