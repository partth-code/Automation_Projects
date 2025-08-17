from tkinter import Tk ,Frame, Label , Button
from tkinter import filedialog
import os
import mimetypes
import shutil
import csv

class FileOrganizer:
    def __init__(self,root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("300x200")
        
        self.toOrganize = None
        
        self.setup()
        
    def setup(self):
        self.title()
        self.organizer()
    
    def title(self):
        self.topFrame = Frame(self.root , width=200 , bg = 'black')
        self.topFrame.pack(fill='both')
        
        Label(self.topFrame , text = "File Organizer" , font = ('Arial',20,'bold') , fg = 'white',bg = 'black').pack(pady = 20)
    
    def organizer(self):
        self.mainFrame = Frame(self.root , bg= "grey")
        self.mainFrame.pack(fill='both' ,expand=True)
        
        self.mainFrame.grid_columnconfigure(0,weight=1)
        self.mainFrame.grid_columnconfigure(1,weight=2)
        
        Label(self.mainFrame , text = "Select Folder to Organize: " ,font=('Arial',10,'bold'), bg= 'grey' , fg = 'white').grid(row=0 ,column=0, pady=20)
        Button(self.mainFrame , text = "Select Folder" , command= self.select_folder , bg = 'black' , fg = 'white' , border=None).grid(row=0,column=1)
        
        self.displySelectedFolder = Label(self.mainFrame , text=  "No Folder Selected" , bg = 'grey' , fg = 'white')
        self.displySelectedFolder.grid(row = 1, column=0 , pady=10)

        Button(self.mainFrame , text= "organize" , fg = 'white', bg = 'black' , border=None, command=self.organize_folder).grid(row=1,column=1)
        
        self.status = Label(self.mainFrame )
        self.status.grid(row=3 , column=0)
        
    def select_folder(self):
        select_dir = filedialog.askdirectory(title = "Select Directoy")
        
        if select_dir:
            self.toOrganize = select_dir
            self.displySelectedFolder.config(text = select_dir ,fg = "green" )
    
    def organize_folder(self):
        
        files = os.listdir(self.toOrganize)
        files = [file for file in files if os.path.isfile(os.path.join(self.toOrganize,file))]
        
        history = []
        
        

        try:
            for file in files:
                old_file_path = os.path.normpath(os.path.join(self.toOrganize , file))
                mime_type = mimetypes.guess_type(old_file_path)[0]
                ext = os.path.splitext(old_file_path)[1][1:].upper()

                
                print(mime_type)
                if mime_type:
                    mime_type = mime_type.split('/')[0].upper()
                    if ext:
                        new_dir_name = f"{mime_type}/{ext}" 
                    else:
                        new_dir_name = f"{mime_type}/NOEXTENSION"
                else:
                    if ext:
                        new_dir_name = f"UNKNOWN/{ext}"
                    else:
                        new_dir_name = f"UNKNOWN/NOEXTENSION"
                
                new_dir_path = os.path.join(self.toOrganize , new_dir_name)
                
                os.makedirs(new_dir_path , exist_ok=True)
                
                new_file_path = os.path.normpath( os.path.join(new_dir_path , file))
                print(new_file_path)
                
                history.append((old_file_path , new_file_path))
                # shutil.move(old_file_path,new_file_path)
                
            history_file = os.path.normpath(os.path.join(self.toOrganize , 'Path_History.csv'))
            
            with open( history_file, 'w',newline="", encoding='utf-8') as file:
                writer =csv.writer(file)
                writer.writerows(history)
            
            self.status.config(text = f"Organized Provided Folder" , fg = 'green')    
                
        except Exception as e:
            self.status.config(text = "An Error Occoured" , fg = 'red')
            print(e)
            
            
                        

if __name__ == "__main__":
    root = Tk()
    app = FileOrganizer(root)
    root.mainloop()