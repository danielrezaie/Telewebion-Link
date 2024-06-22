import os

# Variables for setup
filename = 'Telewebion_Embed_Links.txt'
folder_name = 'htmls'
log_file_name = 'default.html'
prefix1 = '''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>'''
prefix2 = '''</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;
        }
        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
    </style>
</head>
<body>
    <iframe id="videoFrame" src="https://telewebion.com/embed/live/'''
suffix = '''?autoplay=true" allow="autoplay" allowfullscreen></iframe>\n    <script>\n        window.onload = function() {\n            var frame = document.getElementById("videoFrame");\n            frame.onload = function() {\n                var playerDocument = frame.contentDocument || frame.contentWindow.document;\n\n                // Example of hiding elements - you need to know the exact classes or IDs\n                var adElements = playerDocument.getElementsByClassName("ad-class"); // Replace "ad-class" with the actual class name\n                for (var i = 0; i < adElements.length; i++) {\n                    adElements[i].style.display = "none";\n                }\n\n                // You can also remove elements entirely\n                var uiElements = playerDocument.querySelectorAll(".ui-element"); // Replace ".ui-element" with the proper selector\n                uiElements.forEach(function(elem) {\n                    elem.parentNode.removeChild(elem);\n                });\n            };\n        };\n    </script>\n</body>\n</html>\n'''
extension = '''.html'''
log_prefix = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>List of Webpage Links</title>
</head>
<body>
    <h1>List of Webpage Links</h1>
    <ul>'''
filename_prefix = '''<li><a href="./'''
filename_suffix1 = '''" target="_blank">'''
filename_suffix2 = '''</a></li>'''
log_suffix = '''    </ul>
</body>
</html>'''

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
        new_html_file_content = prefix1 + extracted_part + prefix2 + extracted_part + suffix
        
        # Create and write to the HTML file in the specified folder
        with open(os.path.join(folder_name, new_html_file_name), 'w') as new_file:
            new_file.write(new_html_file_content)
        
        # Construct the log entry with the specified prefixes and suffixes
        log_entry = f'{filename_prefix}{new_html_file_name}{filename_suffix1}{extracted_part}{filename_suffix2}'
        
        # Log the HTML file name to the text file
        log_file.write(log_entry + '\n')
        
        # Optionally print a confirmation
        print(f"File created: {new_html_file_name} with content: {new_html_file_content}")
        print(f"Logged file name: {log_entry} to {log_file_name}")
    
    # Write the log suffix at the end of the log file
    log_file.write(f'{log_suffix}\n')
