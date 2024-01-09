import pandas as pd

# Load the Excel file into a DataFrame, specify dtype to force treating columns as strings
file_path = 'data.xlsx'
df = pd.read_excel(file_path, dtype=str, parse_dates=['Fecha de Nacimiento'])

# Add an index to maintain the original order
df['index'] = df.index

# Assume your data is in the first column (column 0) and date in the second column (change 'your_date_column' accordingly)
first_column = df.iloc[:, 0]


# Function to split words based on the rules you provided
def split_names(row):
    words = row.split()

    if len(words) == 2:
        return pd.Series({'apellido': words[0], 'nombre': words[1]})
    elif len(words) == 3:
        return pd.Series({'apellido': words[0], 'nombre': ' '.join(words[1:])})
    elif len(words) == 4:
        return pd.Series({'apellido': ' '.join(words[:2]), 'nombre': ' '.join(words[2:])})
    else:
        # Add more cases as needed
        return pd.Series({})


# Apply the function to create new columns
df[['apellido', 'nombre']] = first_column.apply(split_names)

# Reset the index to the original order
df = df.sort_values(by='index').drop(columns='index').reset_index(drop=True)

# Save the updated DataFrame to a new Excel file with the same name
output_file_path = 'data_output.xlsx'
df.to_excel(output_file_path, index=False)

print("Data separated and saved to", output_file_path)
