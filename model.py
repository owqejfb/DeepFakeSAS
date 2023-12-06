import pandas as pd
import re

def remove_http_substrings(text):
    """
    Remove substrings starting with 'http' and continuing until a whitespace character.

    Parameters:
    text (str): The text from which to remove the substrings.

    Returns:
    str: The text with the substrings removed.
    """
    return re.sub(r'http\S*', '', text)

def get_strings_from_column(file_path, column_name):
    """
    Extract all strings from a specified column in an Excel file and return them as a list.

    Parameters:
    file_path (str): The path to the Excel file.
    column_name (str or int): The name or index of the column to extract strings from.

    Returns:
    list: A list of strings found in the specified column.
    """
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Select the desired column
        column_data = df[column_name]

        # Filter out non-string values and convert to list
        string_list = [remove_http_substrings(item.replace("-&gt", "\b")).lstrip().rstrip() for item in column_data if isinstance(item, str)]

        return string_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Usage example
file_path = 'tweets.xlsx'  # Replace with your file path
column_name = 'Text'  # Replace with your column name or index
string_list = get_strings_from_column(file_path, column_name)

if string_list is not None:
    count = 0
    for string in string_list:
        print(str(count)+". "+string+"\n")
        count +=1
