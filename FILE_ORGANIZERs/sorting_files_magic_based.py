import os
import shutil
import csv
import magic
import re
import mimetypes

'''
Selecting the Folder
listing the fills in dir
creating the organized folders
moving to the folder
'''

def senitize_folder_name(name):
    
    return re.sub('[<>"/\\|?*]',',',name)

def sort_file_by_magic(base_file_path):
    
    history = [] #Path History
    
    folder_content = os.listdir(base_file_path) 
    
    mime = magic.Magic(mime=True)
    
    for file in folder_content:
        
        old_file_path = os.path.join(base_file_path,file)

        
        if not all(ord(c) < 128 for c in file):  # Skip Unicode names as magic cannot comrihend them correctly
            type,_ = mimetypes.guess_type(file)
            
            if type:
            
                if ('.' in file) and not file.startswith('.'):
                    extension = file.split('.')[-1].upper()
                
                else:
                    extension = "NO_EXTENSION"
            else:
                type = "UNKNOWN"
                if ('.' in file) and not file.startswith('.'):
                    extension = file.split('.')[-1].upper()
                else:
                    extension = "NO_EXTENSION"
                
            new_folder = os.path.join(base_file_path,rf'{type.split('/')[0].upper()}\{extension}')
            os.makedirs(new_folder,exist_ok=True)
                    
            new_file_path = os.path.join(new_folder,file)
            print(new_file_path)        
            history.append([old_file_path,new_file_path])
            continue


        
        #Checking if content is file
        if os.path.exists(old_file_path) and os.path.isfile(old_file_path):  
               
                file_type = mime.from_file(old_file_path).split('/')[0].upper()
               
                if file_type:
                    if ('.' in file) and not file.startswith('.'):
                        extension = file.split('.')[-1].upper()

                        new_dir = rf'{file_type}\{extension}'
                    else:
                        
                        new_dir = rf'{file_type}\NO_EXTENSION'   
                
                else:
                    if('.' in file)and not file.startswith('.'):
                        extension = file.split('.')[-1].upper()
                        
                        new_dir = rf'UNKNOWN\{extension}'
                    else:
                        
                        new_dir = rf'UNKNOWN\NO_EXTENSION'
                           
                new_folder  = os.path.join(base_file_path,new_dir)
                os.makedirs(new_folder,exist_ok = True)      
                
                new_file_path = os.path.join(new_folder,file)
                
                try:
                    #Moving and Storing History
                    # shutil.move(old_file_path,new_file_path)
                    history.append([old_file_path,new_file_path])
                
                except Exception as e:
                    print("An Error Occured while moving the file: ",e)
                          
    with open('Path_History.csv','w',newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Old_File_Path','New_File_Path'])
        writer.writerows(history)

if __name__ == "__main__":
    path  = r"C:\Users\parth\Downloads"
    sort_file_by_magic(path)