from PyPDF2 import PdfReader ,PdfWriter
from tkinter import Tk, Frame ,Label,Entry,Button,StringVar
from tkinter import filedialog
import os



'''
To Do -:
1) Selecting the operation
2) Then Select the Files 
3) Then show file path 
4) ask for the file names
5) click perform

'''
class PdfEditor:
    
    def __init__(self,root):
        self.root = root
        self.root.title("PdfEditor")
        self.root.geometry("800x500")
        
        self.filesToJoin = None
        self.outFolder = '\\'
        
        self.tab = 1
        
        self.setup()
        
    
    def setup(self):
        self.tabsFrame = Frame(self.root , bg = 'white' , height= 20)
        self.tabsFrame.pack(fill='x')
        
        self.tabs()
        self.load_tab_content()
        
        
        
        
    def pdfmergergui(self):
        Label(self.tab1Frame , text = "This is Pdf Merger" , font = ('Airal',12,'bold') , bg = 'lightgreen').pack(pady = 10)
        self.file = Button(self.tab1Frame , text = "Select Pdf Files",command = self.selectpdfforjoining)
        self.file.pack(pady = 10)
    
        self.selectedFilesForJoining = Label(self.tab1Frame , text = f"No Files Selected", bg = 'lightgreen')
        self.selectedFilesForJoining.pack(pady=10 )
        
        Label(self.tab1Frame , text = "--------------" , font = ('Airal',12,'bold') , bg = 'lightgreen').pack(pady = 10)
        
        self.mergedFileName = StringVar()
        Label(self.tab1Frame , text = "Enter name for the Outputfile(Eg: output): " , bg = 'lightgreen').pack(pady = 10)
        self.outputnameM = Entry(self.tab1Frame , width=30 , textvariable=self.mergedFileName)
        self.outputnameM.pack(pady = 10)
        
        self.ofolder = Button(self.tab1Frame , text = "Select Output Folder",command = self.destlocation)
        self.ofolder.pack(pady = 10)
        
        self.outfolder = Label(self.tab1Frame , text = f"No Folder Selected", bg = 'lightgreen')
        self.outfolder.pack(pady=10 )
        
        Button(self.tab1Frame , text = "Merge",command = self.merge).pack(pady = 10)
        
        self.mrgmsg = Label(self.tab1Frame , bg = 'lightgreen')
        self.mrgmsg.pack(pady=5)        
        
        # self.selectedfiles = '\n'.join(self.filesToJoin

    
    def pdfsplittergui(self):
        Label(self.tab2Frame , text = "This is Pdf Splitter" , font = ('Airal',12,'bold') , bg = 'lightblue').pack(pady = 10)
        
        
        Button(self.tab2Frame , text = "Select Pdf to Split"  , command=self.selectedFilesForSplitting).pack(pady = 10)
        
        
        self.toSplitPdf = Label(self.tab2Frame , text = "No Pdf Selected" , bg = "lightblue"  )
        self.toSplitPdf.pack(pady=5)        
        
        Label(self.tab2Frame , text = "--------------" , font = ('Airal',12,'bold') , bg = 'lightblue').pack(pady = 10)
        
        self.splitPrefix = StringVar()
        
        Label(self.tab2Frame , text = "Enter name for the Outputfile prefix(Eg: prefix): " , bg = 'lightblue').pack(pady = 10)
        self.splitPrefixEntry = Entry(self.tab2Frame , width=30, textvariable= self.splitPrefix)
        self.splitPrefixEntry.pack(pady=2)
        Button(self.tab2Frame , text = "Select Output Folder" , command=self.split_output_dir).pack(pady=10)
        
        self.splitFolder = Label(self.tab2Frame , text = "No Folder Selected", bg = "lightblue")
        self.splitFolder.pack(pady = 10)
        
    
        
        Button(self.tab2Frame , text = "Split" , command=self.split).pack(pady = 10)
        
        
        self.spltmsg = Label(self.tab2Frame , bg = 'lightblue')
        self.spltmsg.pack(pady=5)   
        
        
    def selectpdfforjoining(self):
        self.filesToJoin = filedialog.askopenfilenames(
            title = "Select one or more files",
            filetypes=[('Pdf Files' , '*.pdf')]
        )    
        
        if self.filesToJoin:
            self.selectedFilesForJoining.config(text = '\n'.join(self.filesToJoin))
    
    
    
    def mergepdf(self, pdf_list , file_name = 'output'):
        writer =PdfWriter()
        
        for pdf in pdf_list:
            reader = PdfReader(pdf)
            for page in reader.pages:
                #in python we reassign local varible in afunction in local scope but cannot adit a global variable
                writer.add_page(page)
            
            
        with open(os.path.join(self.outFolder,f"{file_name}.pdf"),'wb') as file:
            writer.write(file)
        
        self.mrgmsg.config(text = "PDFs merged successfully" , fg = "black")
           
             
    
    
    def destlocation(self): #locationn of destination folder
        self.outFolder = filedialog.askdirectory(title = "Select Folder")
        
        if self.outFolder:
            self.outfolder.config(text = self.outFolder)  
        
    
    def  merge(self):
        name = self.mergedFileName.get() if self.mergedFileName.get() else "output"
        self.mergepdf(self.filesToJoin , name)
      
    
    def selectedFilesForSplitting(self):
        file = filedialog.askopenfilename(title="Select Pdf File" , filetypes= [("Pdf Files",  "*.pdf") , ("All Files" , "*.*")])
        
        if file:
            self.toSplitPdf.config(text=file)
            self.toSplit = file

    
    def split_output_dir(self):
        outDir = filedialog.askdirectory(title="Select Output Folder")
        
        
        if outDir:
            self.splitFolder.config(text=outDir)
            self.splitDir = outDir

    def split_pdf(self,pdf , prefix = "output"):
        
        reader = PdfReader(pdf)
        for i,page in enumerate(reader.pages ,start=1):
            writer = PdfWriter()
            writer.add_page(page)
            
            with open(os.path.join(self.splitDir , f"{prefix}_{i}.pdf") , 'wb') as file:
                writer.write(file)


        self.splitmsg.config(text = "Splitted PDF successfully" , fg = "black")
    
    
    def split(self):
        prefix  = self.splitPrefix.get() if self.splitPrefix.get() else "output"
        
        self.split_pdf(self.toSplit , prefix)
        
    
    def tabs(self):
        self.mrgBtn = Button(self.tabsFrame , text = "merger" , bg='lightgreen' , bd = 0 , command= lambda: self.switch_tab(1))
        self.mrgBtn.grid(row=0,column=0 , sticky='nw')
        
        self.spltBtn = Button(self.tabsFrame , text = "splitter" , bg= 'lightblue' , bd = 0 , command= lambda: self.switch_tab(2))
        self.spltBtn.grid(row=0,column=1 , sticky='nw')
        

    def switch_tab(self,value):
        self.tab = value
        
        for widged in self.root.winfo_children():
            if widged != self.tabsFrame:
                widged.destroy()
        
        self.load_tab_content()
    
    
    def load_tab_content(self):
        
        if(self.tab == 1 ):
            
            self.tab1Frame = Frame(self.root , bg = 'lightgreen',height= 200)
            self.tab1Frame.pack(fill='both',expand=True)
            self.pdfmergergui()
            self.spltBtn.config(bg = "#58a6ba")
            self.mrgBtn.config(bg = "lightgreen")

        else:
            
            self.tab2Frame = Frame(self.root , bg = 'lightblue' , height= 200)
            self.tab2Frame.pack(fill='both',expand=True)
            self.pdfsplittergui()
            self.mrgBtn.config(bg = "#58ba65")
            self.spltBtn.config(bg = "lightblue")
        

        
        
        
if __name__ == "__main__":
    root = Tk()
    app = PdfEditor(root)
    root.mainloop()