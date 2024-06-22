import os

# Variables for setup
filename = 'Telewebion_Embed_Links.txt'
folder_name = 'htmls'
log_file_name = 'AAAAlog.txt'
prefix = 'gay'
suffix = 'gay'
extension = '.html'
log_prefix = 'big1'
filename_prefix = 'nig1'
filename_suffix = 'nig2'
log_suffix = 'big2'

# Ensure the output folder exists
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Open the file and read each line
with open(filename, 'r') as file, open(os.path.join(folder_name, log_file_name), 'w') as log_file:
    # Write the log prefix at the start of the log file
    log_file.write(f'{log_prefix}\n')
    
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
        
        # Construct the log entry with the specified prefixes and suffixes
        log_entry = f'{filename_prefix}{new_html_file_name}{filename_suffix}'
        
        # Log the HTML file name to the text file
        log_file.write(log_entry + '\n')
        
        # Optionally print a confirmation
        print(f"File created: {new_html_file_name} with content: {new_html_file_content}")
        print(f"Logged file name: {log_entry} to {log_file_name}")
    
    # Write the log suffix at the end of the log file
    log_file.write(f'{log_suffix}\n')
