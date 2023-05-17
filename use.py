import matchmaker
import pandas as pd
import os

# Description:
# Input: a list of preferences stored in list.xlsx (name, pref1 to prefn)
# Output: the outcome using stable roommate matching

# Get the full path to the Excel file
file_path = os.path.abspath('list.xlsx')
# Read the Excel file into a pandas DataFrame
df = pd.read_excel(file_path)
# Set the index to the 'name' column and convert to a dictionary
data = df.set_index('name').T.to_dict('list')
print(data)

# preference list
prefs = {
    'Alice': ['Bob', 'Charlie', 'David'],
    'Bob': ['Charlie', 'Alice', 'David'],
    'Charlie': ['David', 'Bob', 'Alice'],
    'David': ['Charlie', 'Bob', 'Alice']
}

# execute the match!!
matchmaker.execute(prefs)