student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
# print(data.head())
letter = data.letter.to_list()
code = data.code.to_list()
df=pandas.DataFrame({'letter':letter,"codes":code})
new_dict={row.letter:row.codes for (index,row) in df.iterrows()}
print(new_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user=input("Enter a word").upper()

new_list=[ new_dict[i] for i in user]
print(new_list)