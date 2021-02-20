import os
import shutil

source = "/Users/Jacob/Whitehatprojects/Class99/file1.rtf"
destination = "/Users/Jacob/Whitehatprojects/Class99/Files"

enterDirectory = input("Enter the directory path")

listOfFiles = os.listdir(enterDirectory)

for i in listOfFiles:
     myExtensions = os.path.splitext(i)
     print( "FirstFile" + myExtensions[0] + "FileExtension" + myExtensions[1] )

     if myExtensions[1] != '':
         ext = myExtensions[1].replace('.', '')
         print(ext)
         if os.path.exists(enterDirectory + '/' + ext):
             shutil.move(enterDirectory + '/' + i, enterDirectory + '/' + ext)
         else:
             os.makedirs(enterDirectory + '/' + ext)
             shutil.move(enterDirectory + '/' + i, enterDirectory + '/' +  ext)
     else:
         continue


# shutil.copy(source, destination)

# shutil.move(source, destination)

# print("Successfully copied")