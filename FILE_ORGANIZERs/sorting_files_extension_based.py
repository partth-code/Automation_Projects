import os
import shutil  #shutil methods dont create folders
import csv


#To Sort File Via Extension
'''
. Selectling the folder to perform sort
.listing the files int the folder
.creating a new flder to storethe specific kind of files on the basis of their extension
.storing the path history in csv file
.storingt the files into respective folders
'''

def sort_files_by_extension(base_folder_path):
    
    #Listing the files in Folder
    folder_content = os.listdir(base_folder_path)
    
    history = [] #To store File History
    print("Starting File Organization...")
    
    
    for file in folder_content:
        
        #Checking if the Content is File or Not
        if(os.path.exists(os.path.join(base_folder_path,file)) and os.path.isfile(os.path.join(base_folder_path,file))):
            
            #Creating Folders To Store Files
            if ('.' in file) and not file.startswith('.'):
                extension = file.split('.')[-1].upper()
            else:
                extension = 'NO_EXTENSION'
                
            new_dir =os.path.join(base_folder_path,extension)
            os.makedirs(new_dir,exist_ok=True)
            
            old_file_path = os.path.join(base_folder_path,file)
            new_file_path = os.path.join(new_dir,file)
            
  
            
            try:
                #Storing Path History and Moving Files
                history.append([old_file_path,new_file_path]) 
                shutil.move(old_file_path,new_file_path) 
            
            except Exception as e:
                print("An Error occccured: ",e)
    
    
    #Storing Path  Hsitory in csv File
    with open(os.path.join( base_folder_path,'Path_History.csv'),'w',encoding ='utf-8') as file:
        writer =  csv.writer(file)
        
        writer.writerow(['Old_File_Path','New_File_Path'])
        writer.writerows(history)


if __name__ == "__main__":
    path  = input("Enter path of folder you wnat to organnize: ")
    sort_files_by_extension(path)
    print("Done File Organization..")
    