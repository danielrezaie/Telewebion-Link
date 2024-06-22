# Open the file and read each line
with open('Telewebion_Embed_Links.txt', 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Strip off any extra whitespace or newline characters
        current_line = line.strip()
        
        # Extract the last part of the URL after the last '/'
        extracted_part = current_line.split('/')[-1]
        
        # Print the extracted part
        print(extracted_part)
        
        # Modify the extracted part to have '.html' at the end
        modified_part = extracted_part + '.html'
        
        # Print the modified part
        print(modified_part)
