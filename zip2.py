import os
import zipfile
import xml.etree.ElementTree as ET


def extract_xml_from_zip(folder_path):
    extract_path = os.path.join(folder_path, "extracted_xml")
    os.makedirs(extract_path, exist_ok=True)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith('.zip'):
            print("yes")
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)

    xml_files = [os.path.join(extract_path, file) for file in os.listdir(extract_path) if file.endswith('.txt')]
    return xml_files


# Example usage
folder_path = "F:\PYTHON\INTERN"

extracted_xml_files = extract_xml_from_zip(folder_path)
print(extracted_xml_files)
for xml_file in extracted_xml_files:
    print(xml_file)

