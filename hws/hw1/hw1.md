*Assignments in this class are individual. While you may discuss ideas with others, you must submit your own individual effort.*

# Goal

The goal of this assignment is to gain proficiency in GitHub usage and to acquire basic skills in writing shell scripts.


## 1. Authenticate to GitHub from the command line
Follow detailed instructions from the lecture on how to authenticate to GitHub and clone the hw1 repo. After you write the script `file_organizer.sh`, commit the script to the repo.


## 2. File Organizer
The objective of this assignment is to create a shell script that organizes files in a specified directory based on their file types.

### Instructions:

### (a) Create a Shell Script:
- Write a shell script named file_organizer.sh.
### (b) Requirements:
- The script should accept a single argument, which is the directory path to be organized.
- It should organize files in the specified directory based on their file types (e.g., images, documents, videos).
### (c) Organizing Files:
- Identify different file types (e.g., images, documents, videos) using shell commands such as file.
- Create separate directories within the specified directory for each file type (e.g., images, documents, videos).
- Copy files into their respective directories based on their file types.
### (d) Handling Existing Directories:
- If directories for specific file types already exist, the script should move files into those directories instead of creating new ones.
### (e) Output:
- After running the script, the specified directory should be organized with files grouped into appropriate directories based on their types.
- Test your script on the directory `messy_dir` from Canvas.

