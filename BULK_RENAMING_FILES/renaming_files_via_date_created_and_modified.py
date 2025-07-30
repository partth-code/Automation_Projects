import os
from datetime import datetime
import json


def rename_file(folder_path , use_modified_time = False):
    
    naming_history = []
    
    try:
        files = os.listdir(folder_path)
        files = [f for f in files if os.path.isfile(os.path.join(folder_path,f))]
        
        for file_name in files:
            file_path = os.path.join(folder_path,file_name)
            
            timestamp = os.path.getmtime(file_path) if use_modified_time else os.path.getctime(file_path)
            date_str = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%D_%H-%M-%S')
            
            ext = os.path.splitext(file_name)[1]
            
            new_name = f"{date_str}{ext}"
            
            new_path = os.path.join(folder_path,new_name)
            
            naming_history.append((file_path,new_path))
            # os.rename(file_path,new_path)
        
        with open('Naming_History.json','w',encoding='utf-8') as file:
            json.dump(naming_history,file,indent=4)
            
            
    except Exception as e:
        print("An Error Occoured while Renaming: " ,e)


if __name__ == "__main__":
    
    path = r'C:\Users\parth\Downloads'
    rename_file(path)        
        
        