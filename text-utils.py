import csv
import json
import math

def convert_csv_text_to_json(csv_text):
    # Split the CSV text into lines
    lines = csv_text.split("\n")
    
    # Get the header row
    header = lines[0]
    
    # Get the data rows
    data = lines[1:]
    
    # Create a list to store the JSON data
    json_data = []
    
    # Loop through the data rows
    for row in data:
        # Split the row into fields
        fields = row.split(",")
        
        # Create a dictionary for the row
        row_dict = dict(zip(header.split(","), fields))
        
        # Add the dictionary to the JSON data
        json_data.append(row_dict)
    
    # Convert the JSON data to a JSON string
    json_text = json.dumps(json_data, indent=1)
    
    return json_text




def convert_csv_string_to_markdown(csv_string):
    # Parse the CSV string
    reader = csv.reader(csv_string.splitlines())
    rows = list(reader)

    # Calculate the maximum length of each column
    col_lengths = [max(len(str(cell)) for cell in col) for col in zip(*rows)]

    # Round up each column length to the nearest multiple of 5
    col_lengths = [math.ceil(length / 5) * 5 for length in col_lengths]

    # Convert each row to a markdown table row
    markdown_rows = [' | '.join(str(cell).ljust(length) for cell, length in zip(row, col_lengths)) for row in rows]

    # Insert the markdown table header separator
    header_separator = ' | '.join('-' * length for length in col_lengths)
    markdown_rows.insert(1, header_separator)

    # Join the rows with newlines
    markdown_table = '\n'.join(markdown_rows)

    return markdown_table


if __name__ == "__main__":
    csv_text = """Name,Age,Location
Alice,25,New York
Bob,30,Los Angeles
Charlie,35,Chicago"""
    
    json_text = convert_csv_text_to_json(csv_text)
    print("JSON Text:")
    print(json_text)
    print()
    
    markdown_text = convert_csv_string_to_markdown(csv_text)
    print("Markdown Text:")
    print(markdown_text)












