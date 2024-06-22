import os

# Variables for setup
filename = 'Telewebion_Embed_Links.txt'
folder_name = 'output_folder'
log_file_name = 'html_file_names.txt'
prefix = 'gay'
suffix = 'gay'
extension = '.html'

# Ensure the output folder exists
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Open the file and read each line
with open(filename, 'r') as file, open(os.path.join(folder_name, log_file_name), 'w') as log_file:
    # Loop through each line in the file
    for line in file:
        # Strip off any extra whitespace or newline characters
        current_line = line.strip()
        
        # Extract the last part of the URL after the last '/'
        extracted_part = current_line.split('/')[-1]
        
        # Construct the filename for the new HTML file
        new_html_file_name = extracted_part + extension
        
        # Construct the content for the new HTML file
        new_html_file_content = prefix + extracted_part + suffix
        
        # Create and write to the HTML file in the specified folder
        with open(os.path.join(folder_name, new_html_file_name), 'w') as new_file:
            new_file.write(new_html_file_content)
        
        # Log the HTML file name to the text file
        log_file.write(new_html_file_name + '\n')
        
        # Optionally print a confirmation
        print(f"File created: {new_html_file_name} with content: {new_html_file_content}")
        print(f"Logged file name: {new_html_file_name} to {log_file_name}")
