import os
from PyPDF2 import PdfReader,PdfWriter


def merge_pdf(pdf_list , output_file = "merged.pdf"):
    writer  = PdfWriter()
    
    for pdf in pdf_list:
        reader = PdfReader(pdf)
        for page in reader.pages:
            writer.add_page(page)
        with open(output_file,'wb') as file:
            writer.write(file)
        
        print("Merged Pdf Saved as Output File")


def split_pdf(pdf_file,output_folder):
    
    reader = PdfReader(pdf_file)
    
    for i,page in enumerate(reader.pages,start=1):
        writer = PdfWriter()
        writer.add_page(page)
        
        output_path = os.path.join(output_folder,f'{i}.pdf')
        
        with open(output_path,'wb') as file:
            writer.write(file)
    
    print(f"Splitted the pdf and stored in folder: {output_folder}")
    

def main():
    
    print("This is a pdf Merger CLI(Command Line Interface)")
    
    
    choice = int(input("Enter '1' to merge pdfs or '2' to split pdf: "))
    
    if choice ==1:
        pdf_list = input("Enter path of all pdf files that you want to merge(seperte them by space): ").strip().split()
        pdf_list = [f.strip() for f in pdf_list]
        output = input("Enter name of output file: ")
            
        merge_pdf(pdf_list,output)
    
    elif choice ==2:
        pdf_file = input("Enter path of the pdf file: ").strip()
        output_folder = input("Enter the path of output folder: ").strip()
        os.makedirs(output_folder,exist_ok = True)
        
        split_pdf(pdf_file,output_folder)
    
    else:
        print("Invalied Choice")
        

if __name__ == "__main__":
    main()

        
        