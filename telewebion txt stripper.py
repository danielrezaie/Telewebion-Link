# Open the file and read each line
with open('Telewebion_Embed_Links.txt', 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Set the string variable to the current line
        current_line = line.strip()  # strip() removes any leading/trailing whitespace, including newlines
        # Print the current line
        print(current_line)
