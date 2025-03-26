import csv
import re

# Filepath to the original CSV containing the author data
csv_file_path = "scopus_data.csv"

# List to store the processed data
processed_data = []

# Read the original CSV file
with open(csv_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header if present
    for row in reader:
        # Column 2 contains the data with names and IDs
        sl_no = row[0]
        author_details = row[2].split(';')  # Split multiple authors in the second column
        
        for author in author_details:
            match = re.match(r"(.+?)\s\((.+?)\)", author.strip())
            if match:
                name, auid = match.groups()
                name = name.replace(',', ";")
                processed_data.append(f"{sl_no}, {name.strip()}, {auid.strip()}")

# Write the processed data to a new file
output_file = "recreated_data.csv"
with open(output_file, 'w') as file:
    file.write("\n".join(processed_data))

# Output message
print(f"Recreated author details saved to '{output_file}'.")
