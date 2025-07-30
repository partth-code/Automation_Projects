import os
import mimetypes
import csv


def rename_file(folder_path,prefix = 'file'):
    """This function renamesthe files in folder"""
    
    naming_history = []
    
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path,f))]
        print(files)
        for count,file_name in enumerate(files,start=1):
            # ext = file_name.split('.')[-1]
            type,_ = mimetypes.guess_type(file_name)
            
            if type:
                type = type.split('/')[0]
            else:
                type = "UNKNOWN"
            
            ext = os.path.splitext(file_name)[1] #more accurate 
            new_name = f"{prefix}_{count}_{type}{ext}"
            
            src = os.path.join(folder_path,file_name)
            dst = os.path.join(folder_path,new_name)
            
            naming_history.append((file_name,new_name))
            # os.rename(src,dst)
            
            print(f'Renamed: {file_name} to {new_name}')
    
    
        with open('Name_History.csv','w',newline = '',encoding = 'utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Old Name' , 'New Name'])
            writer.writerows(naming_history)
            
            
    except Exception as e:
        print("An Error Occoured: ", e)
        
        
if __name__ == "__main__":
    
    path = r'C:\Users\parth\Downloads'
    
    prefix  = input("Enter a prefix for the file name: ")
    
    rename_file(path , prefix)