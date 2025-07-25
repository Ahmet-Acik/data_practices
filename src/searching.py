# searching module
# This module provides functions to search for specific patterns in text files.
import re
def search_in_file(file_path, pattern):
    """
    Search for a specific pattern in a text file.
    
    :param file_path: Path to the text file.
    :param pattern: Regular expression pattern to search for.
    :return: List of lines containing the pattern.
    """
    matches = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if re.search(pattern, line):
                    matches.append(line.strip())
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    return matches

def search_in_directory(directory_path, pattern):
    """
    Search for a specific pattern in all text files within a directory.
    
    :param directory_path: Path to the directory containing text files.
    :param pattern: Regular expression pattern to search for.
    :return: Dictionary with file names as keys and lists of matching lines as values.
    """
    import os
    results = {}
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                matches = search_in_file(file_path, pattern)
                if matches:
                    results[file] = matches
    return results

def search_in_string(text, pattern):
    """
    Search for a specific pattern in a string.
    
    :param text: String to search within.
    :param pattern: Regular expression pattern to search for.
    :return: List of matches found in the string.
    """
    return re.findall(pattern, text)

def search_in_lines(lines, pattern):
    """
    Search for a specific pattern in a list of lines.
    
    :param lines: List of lines to search within.
    :param pattern: Regular expression pattern to search for.
    :return: List of lines containing the pattern.
    """
    matches = []
    for line in lines:
        if re.search(pattern, line):
            matches.append(line.strip())
    return matches


# Example usage:
if __name__ == "__main__":
    # Search for a pattern in a specific file
    file_path = 'example.txt'
    pattern = r'\bPython\b'  # Example pattern to search for the word "Python"
    matches = search_in_file(file_path, pattern)
    print(f"Matches in {file_path}:")
    for match in matches:
        print(match)

    # Search for a pattern in all text files in a directory
    directory_path = 'example_directory'
    results = search_in_directory(directory_path, pattern)
    print(f"Matches in directory {directory_path}:")
    for file, lines in results.items():
        print(f"{file}:")
        for line in lines:
            print(f"  {line}")
    # Search for a pattern in a string
    text = "Python is a programming language. Python is widely used."
    string_matches = search_in_string(text, pattern)
    print(f"Matches in string: {string_matches}")
    
    # Search for a pattern in a list of lines
    lines = [
        "Python is great.",
        "Java is also popular.",
        "Python and Java are both programming languages."
    ]
    line_matches = search_in_lines(lines, pattern)
    print(f"Matches in lines:")
    for line in line_matches:
        print(line)
   