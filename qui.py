import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('path_to_your_file.xml')
root = tree.getroot()

# Find the 'url' element within the 'required_header' element and get its text
url_link = root.find('required_header').find('url').text

# Print the URL
print(url_link)
