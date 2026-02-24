# Name : Dawood Adams
# Date : 24/02/2026
# Program to perform file operations

#create new file 
new_file = open("student data.txt","r+")
new_file.write("{Student name:Dawood Adams, Id :14894067, email adress:adamsdwood363@gmail.com}")
#read to the new file 
data = new_file.read()
print(data)
new_file.close

#delete from the file
#use the os module
import os

os.rmdir("folder_dir")

#