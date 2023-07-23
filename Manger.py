import os
import shutil

print("File Manager")

print("1 - Copy file")
print("2 - Move file")
print("3 - Delete file")
print("4 - Rename file")

option = int(input("Choose option: "))

if option == 1:
  source = input("Enter source file: ")
  dest = input("Enter destination: ")
  shutil.copy(source, dest)
  
elif option == 2:
  source = input("Enter source file: ")
  dest = input("Enter destination: ")
  shutil.move(source, dest)
  
# And so on for other options

print("Task completed!")