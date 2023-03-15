#
# Eduardo R Torres Alamo
# 3/15/2023
# This is a python script made for a specific problem at my current job.
#
import os
import csv

# Set the folder path to read CSV files from
folder_path = 'C:/Users/SMSLO/Desktop/LANDED'

# Iterate over all CSV files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # Set the input filename and output filename
        input_file = os.path.join(folder_path, filename)
        output_file = os.path.splitext(input_file)[0].replace(' ', '') + '_modified.csv'

        # Open the input and output files
        with open(input_file, 'r', newline='') as csv_file, open(output_file, 'w', newline='') as output_csv:
            # Create a CSV reader and writer objects
            reader = csv.reader(csv_file)
            writer = csv.writer(output_csv)

            # Iterate over each row in the CSV file
            for row in reader:
                # Modify the fields in each row
                modified_row = [field.replace(",,,,,,,,,,,,,,,,,,,,,,,", "").replace(', ', ',').replace(' ,', ',').replace('/ ', '/') for field in row]

                # Write the modified row to the output CSV file
                writer.writerow(modified_row)

        print(f'{input_file} was successfully modified and saved as {output_file}')
