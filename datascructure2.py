# Write a program that prompts for a file name,
# then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

# Prompting the user for a file name
file_name = input("Enter the file name: ")

try:
    with open('words.txt', 'r') as file:
        for line in file:
            # Using strip() to remove trailing newline characters
            clean_line = line.rstrip()
            print(clean_line.upper())
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")
except Exception as e:
    print("An error occurred:", e)


