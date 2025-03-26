import csv

name_id_file = "ids_for_author_name.csv" 
authors_data_file = "recreated_data.csv" 

with open(name_id_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        target_author_name = row[0].strip()
        break 

author_id = None
with open(name_id_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        if len(row) >= 2:
            name, _id = row[0].strip(), row[1].strip().split(',')[0]
            if name == target_author_name:
                author_id = _id
                break

if not author_id:
    print(f"Author name '{target_author_name}' not found in '{name_id_file}'.")
    exit()

id_count = 0
name_count = 0

output_file = "result.csv"
with open(authors_data_file, 'r') as csvfile, open(output_file, 'w') as res_file:
    reader = csv.reader(csvfile)
    next(reader)  
    res_file.write("Serial Number, Author name, Author ID")
    for row in reader:
        if len(row) >= 2:
            sl_no = row[0]
            name, _id = row[1].strip(), row[2].strip()
            if _id == author_id:
                id_count += 1
                res_file.write("\n" + sl_no + "," + name + "," + _id)
            if name == target_author_name:
                name_count += 1

self_citation = max(id_count, name_count)
# print(f"Author Name: {target_author_name}")
# print(f"Author ID: {author_id}")
# print(f"Self-Citation Count: {self_citation}")
