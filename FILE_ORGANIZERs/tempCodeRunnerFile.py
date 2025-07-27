import os
import shutil


#To Sort File Via Extension
'''
. Selectling the folder to perform sort
.listing the files int the folder
.creating a new flder to storethe specific kind of files on the basis of their extension
.storingt the files into respective folders
'''

def sort_files_by_extension(base_folder_path):
    
    #Listing the files in Folder
    folder_content = os.listdir(base_folder_path)
    
    for file in folder_content: