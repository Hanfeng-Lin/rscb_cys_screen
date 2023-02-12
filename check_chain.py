import pandas as pd

# Read the Excel file
df = pd.read_excel('uniprot_IDmapping.xlsx')

# Create a new column E for boolean values
df['E'] = False

# Iterate over each row
for index, row in df.iterrows():
    # Get the strings from columns C and D
    string1 = row['chain_id']
    string2 = row['chainID']

    # Remove non-alphabetic characters from the strings
    string1 = ''.join(filter(str.isalpha, string1))
    string2 = ''.join(filter(str.isalpha, string2))

    # Check if all the characters in string1 are included in string2
    is_included = all(char in string2 for char in string1)

    # Set the boolean value in column E
    df.at[index, 'E'] = is_included

# Write the result back to the Excel file
df.to_excel('uniprot_IDmapping.xlsx', index=False)