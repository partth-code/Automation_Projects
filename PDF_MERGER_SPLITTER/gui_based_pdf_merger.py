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
        self.root.geometry("800x400")
        
        self.filesToJoin = None
        self.outFolder = '\\'
        
        self.setup()
        
    
    def setup(self):
        self.topFrame = Frame(self.root , bg = 'lightgreen',height= 200)
        self.topFrame.pack(fill='both',expand=True)
        
        self.bottomFrame = Frame(self.root , bg = 'lightblue' , height= 200)
        self.bottomFrame.pack(fill='both',expand=True)
        
        self.pdfmergergui()
        self.pdfsplittergui()

        

    def pdfmergergui(self):
        Label(self.topFrame , text = "This is Pdf Merger" , font = ('Airal',12,'bold') , bg = 'lightgreen').pack(pady = 10)
        self.file = Button(self.topFrame , text = "Select Pdf Files",command = self.selectpdfforjoining)
        self.file.pack(pady = 10)
    
        self.selectedFilesForJoining = Label(self.topFrame , text = f"No Files Selected", bg = 'lightgreen')
        self.selectedFilesForJoining.pack(pady=10 )
        
        Label(self.topFrame , text = "--------------" , font = ('Airal',12,'bold') , bg = 'lightgreen').pack(pady = 10)
        
        self.mergedFileName = StringVar()
        Label(self.topFrame , text = "Enter name for the Outputfile(Eg: output.pdf): " , bg = 'lightgreen').pack(pady = 10)
        self.outputnameM = Entry(self.topFrame , width=30 , textvariable=self.mergedFileName)
        self.outputnameM.pack(pady = 10)
        
        self.ofolder = Button(self.topFrame , text = "Select Output Folder",command = self.destlocation)
        self.ofolder.pack(pady = 10)
        
        self.outfolder = Label(self.topFrame , text = f"No Folder Selected", bg = 'lightgreen')
        self.outfolder.pack(pady=10 )
        
        Button(self.topFrame , text = "Merge",command = self.merge).pack(pady = 5)        
        
        # self.selectedfiles = '\n'.join(self.filesToJoin

    
    def pdfsplittergui(self):
        Label(self.bottomFrame , text = "This is Pdf Splitter" , font = ('Airal',12,'bold') , bg = 'lightblue').pack(pady = 10)
        
        Button(self.bottomFrame , text = "Select Pdf to Split"  , command=self.selectedFilesForSplitting).pack(pady = 5)
        
        self.toSplitPdf = Label(self.bottomFrame , text = "No Pdf Selected" , bg = "lightblue"  )
        self.toSplitPdf.pack(pady=5)        
        
        self.splitPrefix = StringVar()
        
        self.splitPrefixEntry = Entry(self.bottomFrame , width=30, textvariable= self.splitPrefix)
        self.splitPrefixEntry.pack(pady=2)
        Button(self.bottomFrame , text = "Select Output Folder" , command=self.split_output_dir).pack(pady=5)
        
        self.splitFolder = Label(self.bottomFrame , text = "No Folder Selected", bg = "lightblue")
        self.splitFolder.pack(pady = 5)
        
    
        
        Button(self.bottomFrame , text = "Split" , command=self.split).pack(pady = 5)
        
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
        
        print("Merged Pdf")
           
             
    
    
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


        print("Splitted Pdf")
    
    
    def split(self):
        prefix  = self.splitPrefix.get() if self.splitPrefix.get() else "output"
        
        self.split_pdf(self.toSplit , prefix)
            
        
        
if __name__ == "__main__":
    root = Tk()
    app = PdfEditor(root)
    root.mainloop()