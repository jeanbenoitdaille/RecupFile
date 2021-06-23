import os
     
fichier = "C:/Python36/python.exe"
     

     
extension = os.path.splitext(fichier)[1]
extension = extension.strip(".")
     
print(extension)