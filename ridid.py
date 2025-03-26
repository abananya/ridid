import csv
from collections import defaultdict

csv_file_path = "recreated_data.csv" 
author_to_ids = defaultdict(set)

with open(csv_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        name, author_id = row[1], row[2]
        author_to_ids[name].add(author_id)

output_file = "ids_for_author_name.csv"
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Author Name", "Author IDs"])
    # Write each author's name and associated unique IDs
    for author, ids in author_to_ids.items():
        writer.writerow([author, ",".join(ids)])

print(f"Processed author data and saved to '{output_file}'.")


author_to_ids = defaultdict(set)
with open(csv_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) >= 2:
            name, author_id = row[1].strip(), row[2].strip()
            author_to_ids[author_id].add(name)
# print(author_to_ids)

output_file = "name_for_authors_ids.csv"
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Author Name", "Author IDs"]) 

    for author, ids in author_to_ids.items():
        if len(ids) > 1:  # Check if the author has multiple unique IDs
            writer.writerow([author, ",".join(ids)])

print(f"Processed author data and saved to '{output_file}'.")