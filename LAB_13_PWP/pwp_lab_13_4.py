# Write a Python program that merges the contents of two text files file1.txt and file2.txt into a third file merged.txt. Ensure that the contents of file1.txt come first.

with open (r"C:/Users/abhin/Documents/pwp_lab_13_4.py", 'r') as f1:
    d1 = f1.read ()
with open  (r"C:/Users/abhin/Documents/pwp_lab_13_4.py", 'r') as f2:
    d2 = f2.read ()
    
with open  (r"C:/Users/abhin/Documents/pwp_lab_13_4.py", 'w')as f3:
    f3.write (d1)
    f3.write ("\n")
    f3.write (d2)
    
