# Write a Python program to read a text file line by line and store each line in a list. Print the list after reading the entire file.

with open  (r"C:/Users/abhin/Documents/pwp_lab_13_2.py", 'r') as f1:
    lines = f1.readlines ()

print ("Lines: ", lines)
