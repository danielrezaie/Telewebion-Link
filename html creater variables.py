# Variables for setup
filename = 'Telewebion_Embed_Links.txt'
prefix = 'gay'
suffix = 'gay'
extension = '.html'

# Open the file and read each line
with open(filename, 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Strip off any extra whitespace or newline characters
        current_line = line.strip()
        
        # Extract the last part of the URL after the last '/'
        extracted_part = current_line.split('/')[-1]
        
        # Print the extracted part
        print(extracted_part)
        
        # Modify the extracted part to add the extension
        modified_part = extracted_part + extension
        
        # Print the modified part
        print(modified_part)

        # Further modify the extracted part by adding prefix and suffix
        further_modified_part = prefix + extracted_part + suffix
        
        # Print the further modified part
        print(further_modified_part)
