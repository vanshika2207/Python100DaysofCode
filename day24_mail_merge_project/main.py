# Read the list of names from invited_names.txt
with open('Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

# Read the content of the starting letter template
with open('Input/Letters/starting_letter.txt') as letter_file:
    letter_template = letter_file.read()

# Iterate through each name and create a personalized letter
for name in names:
    # Remove any leading/trailing whitespaces
    name = name.strip()

    # Replace the placeholder [name] with the actual name
    personalized_letter = letter_template.replace('[name]', name)

    # Save the personalized letter to the ReadyToSend folder
    with open('Output/ReadyToSend/{}.txt'.format(name), mode='w') as output_file:
        output_file.write(personalized_letter)