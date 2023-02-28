import os
import re
import subprocess
import sys

# Define the path to the directory containing the Python files
directory_path = sys.argv[1]

# Get a list of all the Python files in the directory
file_names = [f for f in os.listdir(directory_path) if f.endswith(".py")]

# Create a set to store the imported libraries
imported_libraries = set()

# Read the import statements from each Python file
for file_name in file_names:
  file_path = os.path.join(directory_path, file_name)
  with open(file_path, "r") as f:
    file_content = f.read()
    # Use a regular expression to find import statements in the file
    matches = re.findall(r"^import (\w+(?:\.\w+)*)", file_content, re.MULTILINE)
    # Add the imported libraries to the set
    imported_libraries.update(matches)

# Install the imported libraries using pip
for library in imported_libraries:
  subprocess.run(["pip", "install", library])