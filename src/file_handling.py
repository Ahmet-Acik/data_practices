# file handling
import os
import json
from datetime import datetime, timedelta
def read_json_file(file_path):
    """
    Read a JSON file and return its content as a dictionary.
    
    :param file_path: Path to the JSON file
    :return: Dictionary containing the JSON data
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data

def write_json_file(file_path, data):
    """
    Write a dictionary to a JSON file.
    
    :param file_path: Path to the JSON file
    :param data: Dictionary to write to the file
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        
def append_to_json_file(file_path, data):
    """
    Append a dictionary to a JSON file.
    
    :param file_path: Path to the JSON file
    :param data: Dictionary to append to the file
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r+') as file:
        existing_data = json.load(file)
        existing_data.update(data)
        file.seek(0)
        json.dump(existing_data, file, indent=4)
        file.truncate()
        
def read_text_file(file_path):
    """
    Read a text file and return its content as a string.
    
    :param file_path: Path to the text file
    :return: String containing the text file content
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    return content

def write_text_file(file_path, content):
    """Write a string to a text file.
    :param file_path: Path to the text file
    :param content: String to write to the file
    """
    with open(file_path, 'w') as file:
        file.write(content)
        
def append_to_text_file(file_path, content):
    """
    Append a string to a text file.
    
    :param file_path: Path to the text file
    :param content: String to append to the file
    """
    with open(file_path, 'a') as file:
        file.write(content)
        
def file_exists(file_path):
    """
    Check if a file exists at the given path.
    
    :param file_path: Path to the file
    :return: True if the file exists, False otherwise
    """
    return os.path.exists(file_path)

def get_file_modification_time(file_path):
    """
    Get the last modification time of a file.
    
    :param file_path: Path to the file
    :return: Last modification time as a datetime object
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    mod_time = os.path.getmtime(file_path)
    return datetime.fromtimestamp(mod_time)

def get_file_size(file_path):
    """
    Get the size of a file in bytes.
    
    :param file_path: Path to the file
    :return: Size of the file in bytes
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    return os.path.getsize(file_path)

def delete_file(file_path):
    """
    Delete a file at the given path.
    
    :param file_path: Path to the file
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
# main function to demonstrate file handling operations
if __name__ == "__main__":
    # Example usage of file handling functions
    json_file = 'data.json'
    text_file = 'data.txt'
    
    # Write to JSON file
    write_json_file(json_file, {'name': 'Alice', 'age': 30})
    
    # Read from JSON file
    data = read_json_file(json_file)
    print(f"JSON Data: {data}")
    
    # Append to JSON file
    append_to_json_file(json_file, {'city': 'New York'})
    updated_data = read_json_file(json_file)
    print(f"Updated JSON Data: {updated_data}")
    
    # Write to text file
    write_text_file(text_file, "Hello, World!")
    
    # Read from text file
    text_content = read_text_file(text_file)
    print(f"Text Content: {text_content}")
    
    # Append to text file
    append_to_text_file(text_file, "\nThis is a new line.")
    updated_text_content = read_text_file(text_file)
    print(f"Updated Text Content: {updated_text_content}")
    
    # Check if files exist
    print(f"Does {json_file} exist? {file_exists(json_file)}")
    print(f"Does {text_file} exist? {file_exists(text_file)}")
    
    # Get file modification time and size
    print(f"{json_file} last modified at: {get_file_modification_time(json_file)}")
    print(f"{text_file} size: {get_file_size(text_file)} bytes")
    
    # Delete files (uncomment to execute)
    # delete_file(json_file)
    # delete_file(text_file)
    print(f"Deleted files: {json_file} and {text_file}")
    if file_exists(json_file):
        print(f"{json_file} still exists.")
    if file_exists(text_file):
        print(f"{text_file} still exists.")
    else:
        print(f"{text_file} has been deleted.")
    # Note: Uncomment the delete_file calls to actually delete the files.
    # This is just a demonstration, so files are not deleted in this example.
    # End of file handling example
    # Note: Uncomment the delete_file calls to actually delete the files.
    # This is just a demonstration, so files are not deleted in this example.