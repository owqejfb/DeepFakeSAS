import pandas as pd
import re
import json

#https://machinelearningmastery.com/text-generation-with-lstm-in-pytorch/

def remove_http_substrings(text):
    """
    Remove substrings starting with 'http' and continuing until a whitespace character.

    Parameters:
    text (str): The text from which to remove the substrings.

    Returns:
    str: The text with the substrings removed.
    """
    return re.sub(r'http\S*', '', text)

def get_tweets_from_column(file_path, column_name):
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
        string_list = [item.lstrip().rstrip() for item in column_data if isinstance(item, str)]

        return string_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def fix_text(text):
    text = text.replace('&amp;', '&')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    #text = text.replace('\n', '')
    return text

def remove_new_lines(input_string):
    # Split the string by newline characters and return the first part
    return input_string.split('\n')[0]

def write_strings_to_file(file_path, string_list):
    with open(file_path, "w", encoding="utf-8") as file:
        for string in string_list:
            file.write(string + "\n\n")


# Usage example
file_path = 'tweets.xlsx'  # Replace with your file path
column_name = 'Text'  # Replace with your column name or index
tweet_list = get_tweets_from_column(file_path, column_name)

index = 0
for tweet in tweet_list:
    tweet_list[index] =  remove_new_lines(  remove_http_substrings( fix_text(tweet) )).lstrip().rstrip()
    index+=1

index = 1
for tweet in tweet_list:
    print(f"{index}. "+tweet)
    index += 1

write_strings_to_file("sas_tweets.txt", tweet_list)
