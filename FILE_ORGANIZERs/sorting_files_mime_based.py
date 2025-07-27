import os
import shutil
import csv
import mimetypes



#Sorting Folder Via Multipurpose Internet Mail Extensions
def sort_file_by_mime(base_folder_path):
    history = [] #Storing Path History
    
    #Listing Files In Base Directory
    folder_content  = os.listdir(base_folder_path) #Listing Content in Base Folder
    
    for file in folder_content:
        old_file_path = os.path.join(base_folder_path,file)
        
        #Checking if a content is file
        if(os.path.exists(old_file_path) and os.path.isfile(old_file_path)):
            
        
            type,_ = mimetypes.guess_type(file)
            if type:
                type_name =type.split(r'/')[0].upper()
                if ('.' in file) and not file.startswith('.'):
                    extension = file.split('.')[-1].upper()
                    dir_name = rf'{type_name}\{extension}'
                else:
                    dir_name = rf'{type_name}\NO_EXTENSION'
            else:
                if ('.' in file) and not file.startswith('.'):
                    extension = file.split('.')[-1]
                    dir_name = rf'UNKNOWN\{extension}'
                else:
                    dir_name = 'UNKNOWN\NO_EXTENSION'
            
            new_dir  = os.path.join(base_folder_path,dir_name)
            os.makedirs(new_dir,exist_ok=True)
            
            
            new_file_path = os.path.join(new_dir,file)
            
            try:
                #Storing Path History and Moving File
                history.append([old_file_path,new_file_path])
                # shutil.move(old_file_path,ne)
            
            except Exception as e:
                print("An Error Occoured: ",e)
                
    with open('Path_History.csv','w',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Old_File_Path','New_File_Path'])
        writer.writerows(history)
       
    
    
if __name__ == "__main__":
    path  = r"C:\Users\parth\Downloads"
    sort_file_by_mime(path)