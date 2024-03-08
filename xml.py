import os
import re

# Directory containing XML files
directory = 'F:\PYTHON\INTERN\ml_files'

# List to store extracted values
xml_value = []

# Regex pattern to match the <ref-list> tag and its content
pattern_ref_list = r'<ref-list>(.*?)</ref-list>'

# Regex pattern to match the <title> tag
pattern_title = r'<title>(.*?)</title>'

# Loop through XML files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xml'):
        filepath = os.path.join(directory, filename)

        # Open the XML file for reading
        with open(filepath, 'r') as file:
            # Read the file contents
            xml_data = file.read()

            # Search for the <ref-list> tag and extract its content
            matches_ref_list = re.findall(pattern_ref_list, xml_data, re.DOTALL)

            # Remove <title> tags from the extracted content
            for match_ref_list in matches_ref_list:
                # Remove <title> tags
                content_without_title = re.sub(pattern_title, '', match_ref_list)
                xml_value.append(content_without_title)

# Print the extracted values
for value in xml_value:
    print(value)
