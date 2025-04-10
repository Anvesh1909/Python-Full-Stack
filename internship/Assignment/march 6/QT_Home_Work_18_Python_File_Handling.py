
# 1
import os
file_path = "Assignment\march 6\QT_Home_Work_18_Python_File_Handling.txt"
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File does not exist.")




# 2
import os
file_path ="Assignment\march 6\QT_Home_Work_18_Python_File_Handling.txt"
if os.path.exists(file_path):
    print("File size:", os.path.getsize(file_path), "bytes")





# 3
import os
file_path =r"Assignment\march 6\QT_Home_Work_18_Python_File_Handling.txt"
def count_lines(filename):
    with open(filename, "r") as file:
        return len(file.readlines())

if os.path.exists(file_path):
    print("Number of lines:", count_lines(file_path))




# 4
import os
file_path =r"Assignment\march 6\QT_Home_Work_18_Python_File_Handling.txt"
search_term = "Python"
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        for line in file:
            if search_term in line:
                print("Found:", line.strip())




# 5
import os
file_path =r"Assignment\march 6\QT_Home_Work_18_Python_File_Handling.txt"
specific_lines = [4, 8]
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        for i in specific_lines:
            if i <= len(lines):
                print(f"Line {i}: {lines[i-1].strip()}")




# 6
import os
file_path = r"Assignment\march 6\QT_Home_Work_18_Python_File_Handling.txt"

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if "remove this line" not in line:
                file.write(line)




# 7
import os
file_path =r"Assignment\march 6\QT_Home_Work_18_Python_File_Handling.txt"
my_list = ["Apple", "Banana", "Cherry"]
with open("output.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")




# 8
import os
directory_path = "."
print("Files in directory:", os.listdir(directory_path))




# 9
import os
directory_path = "."

print("Number of files:", len(os.listdir(directory_path)))




# 10
import glob
directory_path = "."

print("TXT Files:", glob.glob("*.txt"))




# 11
import os

folder_path = "Assignment\march 6\test_folder"
if os.path.exists(folder_path):
    for file in os.listdir(folder_path):
        os.remove(os.path.join(folder_path, file))
    os.rmdir(folder_path)
    print("Folder deleted.")



# 12
file_path = "C:\Users\manve\Desktop\pythonGit\Python-Full-Stack\internship\Assignment\march 6\QT_Home_Work_18_Python_File_Handling.pdf"
if os.path.exists(file_path):
    print("Created:", os.path.getctime(file_path))
    print("Modified:", os.path.getmtime(file_path))
